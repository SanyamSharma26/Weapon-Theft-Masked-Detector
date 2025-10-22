import os

# Paths to labels
train_labels = "dataset/labels/train"
val_labels = "dataset/labels/val"

# Function to remap
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
                    # Replace class id with 0 (weapon)
                    parts[0] = "0"
                    new_lines.append(" ".join(parts) + "\n")

            with open(path, "w") as f:
                f.writelines(new_lines)

# Remap train and val labels
remap_labels(train_labels)
remap_labels(val_labels)

print("✅ All weapon classes remapped to 'weapon' (class 0).")
