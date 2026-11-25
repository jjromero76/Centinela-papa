import torch
import cv2
from torchvision import transforms, models
import torch.nn as nn

def cargar_modelo_campo(ruta_pesos: str, device: str = "cpu"):
    """Carga el modelo visual para inferencia rápida en campo."""
    base = models.resnet50(weights=None)
    in_feats = base.fc.in_features
    base.fc = nn.Identity()

    class ModeloCampo(nn.Module):
        def __init__(self):
            super().__init__()
            self.backbone = base
            self.proyector = nn.Sequential(nn.Linear(in_feats, 128), nn.ReLU(), nn.Dropout(0.3))
            self.clasificador = nn.Linear(128, 1)

        def forward(self, x):
            return self.clasificador(self.proyector(self.backbone(x)))

    modelo = ModeloCampo().to(device)
    modelo.load_state_dict(torch.load(ruta_pesos, map_location=device))
    modelo.eval()
    return modelo

def predecir_hoja(ruta_imagen: str, modelo, umbral: float = 0.50):
    """Evalúa una fotografía de hoja de papa y retorna probabilidad y alerta."""
    tfms = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    img = cv2.cvtColor(cv2.imread(ruta_imagen), cv2.COLOR_BGR2RGB)
    tensor = tfms(img).unsqueeze(0)
    with torch.no_grad():
        prob = torch.sigmoid(modelo(tensor)).item()
    estado = "ALERTA: Posible Tizón Tardío (Inspeccionar)" if prob >= umbral else "Sin signos de Tizón Tardío"
    return {"probabilidad": round(prob, 4), "diagnostico": estado}