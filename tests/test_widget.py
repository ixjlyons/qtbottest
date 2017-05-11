import pytest
from qtbottest.widget import FormDialog


def test_form_dialog(qtbot):
    attrs = [('attr1', 'Attribute 1'),
             ('attr2', 'Attribute 2')]
    dialog = FormDialog(attrs)
    qtbot.addWidget(dialog)

    qtbot.keyClicks(dialog.line_edits['attr1'], "hiya")
    qtbot.keyClicks(dialog.line_edits['attr2'], "buddy")
    dialog.accept()

    data = dialog.get_data()
    assert data['attr1'] == "hiya"
    assert data['attr2'] == "buddy"
