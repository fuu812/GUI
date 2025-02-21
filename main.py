import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import QDate
import locale
locale.setlocale(locale.LC_TIME, 'Japanese_Japan')

class DateCalculator(QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("返却日表示プログラム")
    self.setGeometry(100, 100, 300, 200)

    layout = QVBoxLayout()

    self.date_input = QLineEdit(self)
    self.date_input.setPlaceholderText("YYYY-MM-DD")
    layout.addWidget(self.date_input)

    self.period_input = QLineEdit(self)
    self.period_input.setPlaceholderText("貸出期間（日数）")
    layout.addWidget(self.period_input)

    self.calculate_button = QPushButton("実行", self)
    self.calculate_button.clicked.connect(self.calculate_date)
    layout.addWidget(self.calculate_button)

    self.result_label = QLabel("結果はここに表示されます", self)
    layout.addWidget(self.result_label)

    self.setLayout(layout)

  def calculate_date(self):
    input_date = self.date_input.text()
    period_text = self.period_input.text()
    try:
      date = QDate.fromString(input_date, "yyyy-MM-dd")
      if not date.isValid():
        raise ValueError("正しくない入力です（入力例：2025-01-01）")

      if not period_text:
        raise ValueError("貸出期間を入力してください")

      period_days = int(period_text)
      new_date = date.addDays(period_days)
      self.result_label.setText(
          f"{period_days}日後の日付: {new_date.toString('yyyy-MM-dd')}")
    except ValueError as e:
      self.result_label.setText(str(e))

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = DateCalculator()
  window.show()
  sys.exit(app.exec())
