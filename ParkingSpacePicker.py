import cv2
import pickle

# Ukuran area parkir
width, height = 107, 48

# Coba muat posisi dari file jika ada
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

# Fungsi untuk klik mouse
def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
                break  # berhenti setelah 1 area terhapus

    # Simpan posisi ke file
    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

# Loop utama
while True:
    img = cv2.imread('carParkImg.png')

    # Gambar area parkir
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup semua jendela OpenCV
cv2.destroyAllWindows()
