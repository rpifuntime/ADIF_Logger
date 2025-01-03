import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Initialize log list
qso_log = []

# Function to save QSO data
def save_qso():
    qso_date = entry_date.get()
    time_on = entry_time.get()
    callsign = entry_call.get()
    band = entry_band.get()
    mode = entry_mode.get()
    rst_sent = entry_rst_sent.get()
    rst_rcvd = entry_rst_rcvd.get()
    comment = entry_comment.get()

    # Validate input
    if not all([qso_date, time_on, callsign, band, mode]):
        messagebox.showerror("Error", "Please fill in all required fields.")
        return

    # Add QSO to log
    qso = {
        "QSO_DATE": qso_date,
        "TIME_ON": time_on,
        "CALL": callsign,
        "BAND": band,
        "MODE": mode,
        "RST_SENT": rst_sent,
        "RST_RCVD": rst_rcvd,
        "COMMENT": comment
    }
    qso_log.append(qso)

    # Clear fields
    entry_date.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    entry_call.delete(0, tk.END)
    entry_band.delete(0, tk.END)
    entry_mode.delete(0, tk.END)
    entry_rst_sent.delete(0, tk.END)
    entry_rst_rcvd.delete(0, tk.END)
    entry_comment.delete(0, tk.END)

    messagebox.showinfo("Success", "QSO saved!")

# Function to export to ADIF
def export_adif():
    if not qso_log:
        messagebox.showerror("Error", "No QSOs to export.")
        return

    file_path = "qso_log.adi"
    with open(file_path, "w") as f:
        f.write("ADIF Export\n<EOH>\n")
        for qso in qso_log:
            f.write(f"<QSO_DATE:{len(qso['QSO_DATE'])}>{qso['QSO_DATE']} ")
            f.write(f"<TIME_ON:{len(qso['TIME_ON'])}>{qso['TIME_ON']} ")
            f.write(f"<CALL:{len(qso['CALL'])}>{qso['CALL']} ")
            f.write(f"<BAND:{len(qso['BAND'])}>{qso['BAND']} ")
            f.write(f"<MODE:{len(qso['MODE'])}>{qso['MODE']} ")
            if qso['RST_SENT']:
                f.write(f"<RST_SENT:{len(qso['RST_SENT'])}>{qso['RST_SENT']} ")
            if qso['RST_RCVD']:
                f.write(f"<RST_RCVD:{len(qso['RST_RCVD'])}>{qso['RST_RCVD']} ")
            if qso['COMMENT']:
                f.write(f"<COMMENT:{len(qso['COMMENT'])}>{qso['COMMENT']} ")
            f.write("<EOR>\n")

    messagebox.showinfo("Export Complete", f"Log exported to {file_path}")

# Create GUI window
root = tk.Tk()
root.title("QSO Logger")

# Create input fields
tk.Label(root, text="QSO Date (YYYYMMDD):").grid(row=0, column=0, sticky="e")
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1)

tk.Label(root, text="Time On (HHMMSS UTC):").grid(row=1, column=0, sticky="e")
entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1)

tk.Label(root, text="Callsign:").grid(row=2, column=0, sticky="e")
entry_call = tk.Entry(root)
entry_call.grid(row=2, column=1)

tk.Label(root, text="Band:").grid(row=3, column=0, sticky="e")
entry_band = tk.Entry(root)
entry_band.grid(row=3, column=1)

tk.Label(root, text="Mode:").grid(row=4, column=0, sticky="e")
entry_mode = tk.Entry(root)
entry_mode.grid(row=4, column=1)

tk.Label(root, text="RST Sent:").grid(row=5, column=0, sticky="e")
entry_rst_sent = tk.Entry(root)
entry_rst_sent.grid(row=5, column=1)

tk.Label(root, text="RST Received:").grid(row=6, column=0, sticky="e")
entry_rst_rcvd = tk.Entry(root)
entry_rst_rcvd.grid(row=6, column=1)

tk.Label(root, text="Comment:").grid(row=7, column=0, sticky="e")
entry_comment = tk.Entry(root)
entry_comment.grid(row=7, column=1)

# Add buttons
tk.Button(root, text="Save QSO", command=save_qso).grid(row=8, column=0, pady=10)
tk.Button(root, text="Export to ADIF", command=export_adif).grid(row=8, column=1, pady=10)

# Run the GUI loop
root.mainloop()
