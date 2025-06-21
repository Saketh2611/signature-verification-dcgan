# ✍️ Signature Verification using DCGAN

This project uses **Deep Convolutional Generative Adversarial Networks (DCGANs)** to perform two key tasks in the context of signature-based authentication:

- 🧠 **Signature Synthesis** – generating realistic handwritten signatures.
- 🔍 **Signature Verification** – detecting whether a given signature is real or forged.

---

## 📘 Project Summary

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
     Real Signature: ✅ Real (Score: 0.7772)
     Forged Signature: ❌ Fake (Score: 0.0021)
     ```

---

## 📊 Results

- **Histograms of verification scores** clearly show separation between real and fake signatures.
- The system learns realistic patterns in handwriting and performs well even on unseen forged examples.

![Histogram of scores](./assets/verification_histogram.png)
*(Higher score = more confident it is real)*

- The generator produces synthetic signatures that closely resemble the originals, useful for augmentation or signature modeling.

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

## 🎓 Author

Saketh Vaddiparthi — BTech Aerospace Engineering, IIT Madras  
Currently exploring AI for document and ID verification systems 🚀
