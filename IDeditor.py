# ライブラリのインポート
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pydicom

def load_dicom():
    dicom_directory = filedialog.askdirectory()
    if dicom_directory:
        try:
            dicom_files = [os.path.join(dicom_directory, filename) for filename in os.listdir(dicom_directory)]
            if not dicom_files:
                messagebox.showwarning("Warning", "No files found in the selected directory.")
                return
            dicom_series = []
            for dicom_file in dicom_files:
                ds = pydicom.dcmread(dicom_file)
                dicom_series.append(ds)
            if dicom_series:
                patient_id.set(dicom_series[0].PatientID)
                patient_name.set(dicom_series[0].PatientName)  # 患者の名前を読み込む
                acquisition_date.set(dicom_series[0].get("AcquisitionDate", "N/A"))  # 撮像時期を読み込む
            messagebox.showinfo("Success", f"情報を読み込みました")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load files: {str(e)}")

def save_dicom():
    if not patient_id.get():
        messagebox.showwarning("Warning", "Patient ID is empty.")
        return

    dicom_directory = filedialog.askdirectory()
    if dicom_directory:
        try:
            dicom_files = [os.path.join(dicom_directory, filename) for filename in os.listdir(dicom_directory)]
            if not dicom_files:
                messagebox.showwarning("Warning", "No files found in the selected directory.")
                return
            for dicom_file in dicom_files:
                ds = pydicom.dcmread(dicom_file)
                ds.PatientID = patient_id.get()
                ds.PatientName = patient_name.get()  # 患者の名前を更新
                ds.Aquisition_date = acquisition_date.get()
                ds.save_as(dicom_file)  # 同じファイルに上書き保存
            messagebox.showinfo("Success", f"情報が更新されました")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save modified files: {str(e)}")

# GUIの作成
root = tk.Tk()
root.title("DICOM ID and Name Editor")

# フレーム
frame = tk.Frame(root)
frame.pack(padx=50, pady=50)

# ラベルとエントリ
tk.Label(frame, text="ID :").grid(row=1, column=0, sticky="E")
patient_id = tk.StringVar()
tk.Entry(frame, textvariable=patient_id).grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame, text="Name :").grid(row=2, column=0, sticky="E")
patient_name = tk.StringVar()
tk.Entry(frame, textvariable=patient_name).grid(row=2, column=1, padx=10, pady=10)

# 撮像時期を表示（編集不可）
tk.Label(frame, text="Acquisition Date:").grid(row=3, column=0, sticky="E")
acquisition_date = tk.StringVar()
tk.Entry(frame, textvariable=acquisition_date).grid(row=3, column=1, padx=10, pady=10)


# ボタン
tk.Button(frame, text="読み込み", command=load_dicom).grid(row=5, column=1, pady=10)
tk.Button(frame, text="更新", command=save_dicom).grid(row=6, column=1, pady=10)

# ウィンドウを表示
root.mainloop()