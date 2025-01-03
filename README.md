# ADIF_Logger
log qso's ad export as adif

### **How It Works**
1. **QSO Logging**:
   - Enter details such as date, time, callsign, band, mode, and signal reports.
   - Click "Save QSO" to add the QSO to the log.

2. **Export to ADIF**:
   - Click "Export to ADIF" to generate an ADIF file named `qso_log.adi` in the same directory as the script.

3. **Input Validation**:
   - The program ensures required fields are filled in before saving a QSO.

4. **ADIF File Structure**:
   - Each QSO is formatted in ADIF for compatibility with QRZ and other logging systems.

---

### **Dependencies**
This script uses only standard Python libraries (`tkinter` for the GUI and `datetime` for time handling). No additional installation is required.

