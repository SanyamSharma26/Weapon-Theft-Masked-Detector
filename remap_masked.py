import os

# update paths if needed
train_labels = "masked_face_dataset/train/labels"
val_labels = "masked_face_dataset/valid/labels"

def remap_labels(label_folder):
    for file in os.listdir(label_folder):
        if file.endswith(".txt"):
            path = os.path.join(label_folder, file)
            with open(path, "r") as f:
                lines = f.readlines()

            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 5:
                    parts[0] = "1"  # set class ID = 1 for masked_face
                    new_lines.append(" ".join(parts) + "\n")

            with open(path, "w") as f:
                f.writelines(new_lines)

remap_labels(train_labels)
remap_labels(val_labels)
print("✅ Masked face dataset remapped to class 1 (masked_face).")
