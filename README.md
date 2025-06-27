# ✍️ Signature Verification using DCGAN
## 📁 Dataset

The dataset used in this project contains:

- `full_org/` – 1000+ original handwritten signature images  
- `full_forg/` – 1000+ forged signature images

To keep the GitHub repository lightweight, the full dataset is hosted on Google Drive:

👉 [Download Full Signature Dataset (Google Drive)](https://drive.google.com/file/d/1CAjtavJerVnrObpj10GHT4P-muqILVL7/view?usp=sharing)

If you're running the project on Google Colab, you can mount this Drive folder directly to load the dataset into your notebook.
## 🌐 Web Interface

This project includes a web UI to upload and verify signatures using the trained model.

🚀 Backend API: Built using FastAPI (see [`main_1.py`](./main_1.py))  
🎨 Frontend UI: Deployed static demo here 👉 [Signature UI Demo](https://Saketh2611.github.io/signature-verification-ui/)


> Note: The demo is only the HTML UI. For full functionality, clone the repo and run the FastAPI server locally.
 In command prompt type uvicorn main_1:app --reload
 You can watch the video bandicam 2025-06-21 15-14-26-783.mp4 to look how its working




This project uses **Deep Convolutional Generative Adversarial Networks (DCGANs)** to perform two key tasks in the context of signature-based authentication:

- 🧠 **Signature Synthesis** – generating realistic handwritten signatures.
- 🔍 **Signature Verification** – detecting whether a given signature is real or forged.

---

## 📘 Problem Statement

In academic institutions, each student submits a signature sample as identity proof. During exams, students sign attendance sheets. This project proposes an automated system that uses a trained model to verify whether the test-time signature matches the student's original sample — helping prevent impersonation or signature fraud.

---

## 🧠 How It Works

1. **Training Data**  
   The model is trained on a dataset of grayscale signature images:
   - `full_org/` contains original, genuine signatures.
   - `full_forg/` contains forged (fake) signatures.

2. **Model Architecture**
   - A **Generator** learns to synthesize fake signatures from random noise.
   - A **Discriminator** learns to distinguish between real and fake signatures.
   - Together, they improve each other through adversarial training (GAN setup).

3. **Verification System**
   - Once trained, the discriminator acts as a **signature verifier**.
   - Given a test signature, it outputs a confidence score between `0` (fake) and `1` (real).
   - Example:
     ```
     Real Signature: ✅ Real (Score: 0.9541)
     Forged Signature: ❌ Fake (Score: 0.0115)
     ```

---

## 📊 Results

- The entire project was implemented in a **Google Colab notebook** to ensure smooth training using GPU and easy visualization of results.
- The notebook includes:
  - ✅ Sample signature verification outputs with discriminator scores
  - 🧠 Generated synthetic signatures using the trained DCGAN
  - 📈 Histogram comparing the discriminator's confidence on real vs forged signatures
- The discriminator shows a clear ability to differentiate between genuine and fake signatures.
- Generator outputs closely resemble human signatures and can be used for further analysis or synthetic data generation.

---

## ✅ Applications

- 🎓 **Exam Hall Attendance Verification**  
  Instantly verify that the student who signed the sheet is the actual registered person.

- 📝 **Document Authentication**  
  Detect forgeries in important forms, certificates, or contracts.

- 🔒 **Digital Security**  
  Integrate with signature-based access control systems for enhanced identity verification.

---

## 👨‍💻 Built With

- **PyTorch** – for neural network modeling  
- **DCGAN** – Deep Convolutional Generative Adversarial Network  
- **Matplotlib** – for score distribution plots  
- **PIL (Pillow)** – image loading and processing

---


