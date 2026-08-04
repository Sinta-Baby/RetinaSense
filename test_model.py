from models.efficientnet_b3 import build_model

model = build_model()

print("✅ Model created successfully!")
print(model.classifier)