# Модели,которые могут предсказывать результат

# Как добраться до школы: walk / bus / taxi
# Классы:
#   0 = walk  (пешком)
#   1 = bus   (автобус)
#   2 = taxi  (такси)
# distance_km - сколько вам километров до школы
# late_min - на сколько опаздываеш к занятию
# rain_mm - сколько дождя

from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
import matplotlib.pyplot as plt

dataset = []

# --- ПЕШКОМ: недалеко, не опаздываешь, дождя почти нет ---
row = {"distance_km": 0.8, "late_min": 0,  "rain_mm": 0,  "label": "walk"}; dataset.append(row)
row = {"distance_km": 1.2, "late_min": 0,  "rain_mm": 0.5,"label": "walk"}; dataset.append(row)
row = {"distance_km": 1.0, "late_min": 3,  "rain_mm": 0,  "label": "walk"}; dataset.append(row)
row = {"distance_km": 1.4, "late_min": 2,  "rain_mm": 1.0,"label": "walk"}; dataset.append(row)

# --- АВТОБУС: средняя дистанция/погода, опаздываешь немного ---
row = {"distance_km": 3.0, "late_min": 0,  "rain_mm": 0,  "label": "bus"};  dataset.append(row)
row = {"distance_km": 2.5, "late_min": 5,  "rain_mm": 1.5,"label": "bus"};  dataset.append(row)
row = {"distance_km": 4.0, "late_min": 0,  "rain_mm": 3.0,"label": "bus"};  dataset.append(row)
row = {"distance_km": 5.5, "late_min": 4,  "rain_mm": 0,  "label": "bus"};  dataset.append(row)
row = {"distance_km": 2.0, "late_min": 6,  "rain_mm": 0,  "label": "bus"};  dataset.append(row)

# --- ТАКСИ: сильно опаздываешь ИЛИ ливень ИЛИ очень далеко ---
row = {"distance_km": 1.0, "late_min": 12, "rain_mm": 0,  "label": "taxi"}; dataset.append(row)
row = {"distance_km": 2.0, "late_min": 15, "rain_mm": 0,  "label": "taxi"}; dataset.append(row)
row = {"distance_km": 3.0, "late_min": 10, "rain_mm": 0,  "label": "taxi"}; dataset.append(row)
row = {"distance_km": 1.2, "late_min": 0,  "rain_mm": 12, "label": "taxi"}; dataset.append(row)
row = {"distance_km": 8.0, "late_min": 2,  "rain_mm": 0,  "label": "taxi"}; dataset.append(row)

label_to_id = {"walk": 0, "bus": 1, "taxi": 2}
id_to_label = {0: "walk", 1: "bus", 2: "taxi"}
features = ["distance_km", "late_min", "rain_mm"]

X = []
y = []
i = 0
while i < len(dataset):
    row = dataset[i]
    X.append([row["distance_km"], row["late_min"], row["rain_mm"]])
    y.append(label_to_id[row["label"]])
    i += 1

clf = DecisionTreeClassifier(max_depth=3, random_state=0)
clf.fit(X, y)

print("Правила дерева (укороченно):\n")
print(export_text(clf, feature_names=features))


tests = [
    {"distance_km": 1.0, "late_min": 0,  "rain_mm": 0},   # близко, не опаздываешь, сухо → walk
    {"distance_km": 2.8, "late_min": 4,  "rain_mm": 1},   # средне, чуть опоздание → bus
    {"distance_km": 1.2, "late_min": 0,  "rain_mm": 15},  # ливень → taxi
    {"distance_km": 3.5, "late_min": 12, "rain_mm": 0},   # сильное опоздание → taxi
    {"distance_km": 6.0, "late_min": 2,  "rain_mm": 0.5}, # далеко → bus (или taxi, зависит от границ)
]

j = 0
while j < len(tests):
    t = tests[j]
    x = [[t["distance_km"], t["late_min"], t["rain_mm"]]]
    pred = clf.predict(x)[0]
    print("Ситуация:", t, "→", id_to_label[pred])
    j += 1

plt.figure(figsize=(10, 6))
plot_tree(
    clf,
    filled=True,
    feature_names=features,
    class_names=[id_to_label[0], id_to_label[1], id_to_label[2]]
)
plt.title("Как добираться до школы: walk / bus / taxi")
plt.show()