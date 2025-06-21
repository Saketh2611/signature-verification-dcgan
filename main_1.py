from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
import torch
import torchvision.transforms as transforms
import io
from model import Discriminator

app = FastAPI()

# Path for HTML templates
templates = Jinja2Templates(directory="templates")

# Constants
image_size = 64
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Preprocessing transform
transform = transforms.Compose([
    transforms.Resize((image_size, image_size)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

# Load trained discriminator
discriminator = Discriminator()
discriminator.load_state_dict(torch.load(r"C:\Users\v.saketh\Downloads\discriminator.pth", map_location=device))
discriminator.eval()
discriminator.to(device)

# Homepage: Upload interface
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Verification endpoint
@app.post("/verify")
async def verify_signature(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("L")
    image_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        score = discriminator(image_tensor).item()
        prediction = "Real" if score > 0.5 else "Fake"

    return JSONResponse(content={"prediction": prediction, "score": round(score, 4)})
