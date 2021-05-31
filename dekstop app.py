import tkinter as tk
from tkinter import *


class system:
    def __init__(self):
        self.root = Tk()
        self.window(self.root)

    def window(self, root):
        self.master = root
        self.master.title("Prediksi Covid-19")
        self.master.geometry("720x500+100+70")
        self.master.config(bg="bisque3")

        # frame system
        self.frame_system = LabelFrame(self.root, height=480, width=700)
        self.frame_system.place(x=10, y=10)

        # isi di frame system
        # 1. label
        self.title = Label(self.frame_system, text="SELAMAT DATANG DI SISTEM PREDIKSI COVID-19",
                           font=("Times new roman", 15, 'bold'), bg="deepskyblue3", fg="black")
        self.title.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

        # 2. intro
        self.title = Label(self.frame_system, text="Jawab pertanyaan berikut ini sesuai dengan keluhan anda",
                           font=("Times new roman", 12))
        self.title.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        # 3. pertanyaan
        breathing_problem = str(
            "1. Apakah anda mengalami gangguan pernapasan?")
        fever = str("2.Apakah anda mengalami demam (suhu >38 derajat)?")
        dry_cough = str("3. Apakah anda mengalami batuk kering?")
        sore_throat = str("4. Apakah anda mengalami sakit tenggorokan?")
        running_nose = str("Apakah anda mengalami hidung berair")
        asthma = str("Apakah anda memiliki riwayat penyakit asma?")
        cronicc_lung_disease = str(
            "Apakah anda memiliki riwayat penyakit paru-paru kronis?")
        headache = str("Apakah anda mengalami sakit kepala?")
        heart_disease = str("Apakah anda memiliki penyakit jantung?")
        diabetes = str("Apakah anda memiliki riwayat penyakit diabetes?")
        hypertension = str("Apakah anda memiliki hipertensi (darah tinggi)")
        fatigue = str("Apakah anda merasa kelelahan?")
        gastro = str("Apakah anda memiliki masalah pencernaan atau lambung?")
        abroad_travel = str(
            "Apakah anda dalam waktu 14 hari ini melakukan perjalanan keluar negeri?")
        contact = str(
            "Apakah anda pernah melakukan kontak dengan seorang pengidap COVID dalam waktu 14 hari ini?")
        attend_large_gath = str(
            "Apakah dalam waktu 14 hari ini anda menghadiri pertemuan yang dihari oleh banyak orang? ")
        visited_public = str(
            "Apakah dalam waktu 14 hari ini anda mengunjungi tempat publik?")
        fams_working_in_pub = str(
            "Apakah ada keluarga anda yang bekerja di tempat umum?")
        wearing_mask = str("Apakah anda tetap menggunakan masker?")
        sanitation_from_market = str(
            "Apakah anda membersikan/sanitize barang-barang yang dibeli dari supermarket?")

        # pertanyaan 1

        self.title = Label(
            self.frame_system, text=breathing_problem, font=("Times new roman", 12))
        self.title.grid(row=2, column=0,  padx=5, pady=5, sticky=tk.W)
        self.radioYes1 = tk.Radiobutton(self.frame_system, text="Ya",
                                        variable=bool, value="1")
        self.radioNo1 = tk.Radiobutton(self.frame_system, text="Tidak",
                                       variable=bool, value="0")
        self.radioYes1.grid(row=3, column=0, sticky=tk.W)
        self.radioNo1.grid(row=4, column=0,  sticky=tk.W)

        # pertanyaan 2
        self.title = Label(self.frame_system, text=fever,
                           font=("Times new roman", 12))
        self.title.grid(row=5, column=0,  padx=5, pady=5, sticky=tk.W)
        self.radioYes2 = tk.Radiobutton(self.frame_system, text="Ya",
                                        variable=bool, value="1")
        self.radioNo2 = tk.Radiobutton(self.frame_system, text="Tidak",
                                       variable=bool, value="0")
        self.radioYes2.grid(row=6, column=0, sticky=tk.W)
        self.radioNo2.grid(row=7, column=0,  sticky=tk.W)

        # pertanyaan 3
        self.title = Label(self.frame_system, text=dry_cough,
                           font=("Times new roman", 12))
        self.title.grid(row=8, column=0,  padx=5, pady=5, sticky=tk.W)
        self.radioYes3 = tk.Radiobutton(self.frame_system, text="Ya",
                                        variable=bool, value="1")
        self.radioNo3 = tk.Radiobutton(self.frame_system, text="Tidak",
                                       variable=bool, value="0")
        self.radioYes3.grid(row=9, column=0, sticky=tk.W)
        self.radioNo3.grid(row=10, column=0,  sticky=tk.W)

        # pertanyaan 4
        self.title = Label(self.frame_system, text=sore_throat,
                           font=("Times new roman", 12))
        self.title.grid(row=11, column=0,  padx=5, pady=5, sticky=tk.W)
        self.radioYes4 = tk.Radiobutton(self.frame_system, text="Ya",
                                        variable=bool, value="1")
        self.radioNo4 = tk.Radiobutton(self.frame_system, text="Tidak",
                                       variable=bool, value="0")
        self.radioYes4.grid(row=12, column=0, sticky=tk.W)
        self.radioNo4.grid(row=13, column=0,  sticky=tk.W)

        # pertanyaan 5
        self.title = Label(self.frame_system, text=running_nose,
                           font=("Times new roman", 12))
        self.title.grid(row=14, column=0,  padx=5, pady=5, sticky=tk.W)
        self.radioYes5 = tk.Radiobutton(self.frame_system, text="Ya",
                                        variable=bool, value="1")
        self.radioNo5 = tk.Radiobutton(self.frame_system, text="Tidak",
                                       variable=bool, value="0")
        self.radioYes5.grid(row=15, column=0, sticky=tk.W)
        self.radioNo5.grid(row=16, column=0,  sticky=tk.W)

    # buat frame user


if __name__ == '__main__':
    system()
