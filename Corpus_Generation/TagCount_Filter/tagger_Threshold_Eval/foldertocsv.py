import openpyxl
import os

def combine_text_to_excel(folder_path, output_file):
  """
  This function lists filenames of text files in a single column of an Excel file (skipping the first row).

  Args:
    folder_path: Path to the folder containing text files.
    output_file: Path to the output Excel file.
  """
  # Create a new workbook
  wb = openpyxl.Workbook()
  sheet = wb.active
  sheet.title = 'Filenames'

  # Skip first row (header)
  row = 2  # Start writing from row 2

  # Loop through all files in the folder
  for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Check if it's a text file
      # Write filename to the first column (skipping row 1)
      sheet.cell(row=row, column=1).value = filename
      row += 1  # Increment row counter

  # Save the workbook
  wb.save(output_file)

  print(f"Filenames listed in Excel: {output_file}")

# Replace with your actual folder path
folder_path = r"C:\Users\karan\OneDrive - ualberta.ca\Bioin_401\tagger_Threshold_stats\EvalSet"
# Replace with your desired output filename
output_file = 'GTEvalSetFileNames.xlsx'

combine_text_to_excel(folder_path, output_file)

print(f"Filenames listed in Excel: {output_file}")
