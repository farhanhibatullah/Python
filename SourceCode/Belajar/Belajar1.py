import numpy as np

tinggi_berat = [[175, 67], 
                [167, 60],
                [168, 56],
                [170, 57],
                [180, 80]]

updated = [[177, 69],
           [180, 88],
           [156, 50],
           [173, 82],
           [161, 70]]

np_tinggi_berat = np.array(tinggi_berat)
np_updated = np.array(updated)
print(np_tinggi_berat)

daftar_baru = np.concatenate((np_tinggi_berat,np_updated), axis = 0)
print(daftar_baru)
print(np.sort(daftar_baru, axis=0))
tinggi = np_tinggi_berat[:, 0]
nilai_updated = tinggi * 2
print(nilai_updated)
