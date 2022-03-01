import os
import npyscreen as npy

class _FileChooserForm(npy.Form):
    data = npy.NPSTreeData(['0', '1', '2', '3'])
    def afterEditing(self):
        self.parentApp.setNextForm(None)
    def create(self):
        self.myName        = self.add(npy.TitleText, name='Name')
        self.myDepartment = self.add(npy.TitleSelectOne, scroll_exit=True, max_height=3, name='Department', values = ['Department 1', 'Department 2', 'Department 3'])
        self.myDate        = self.add(npy.TitleDateCombo, name='Date Employed')
        self.Tree = self.add(npy.MLTree, values=self.data, name='Tree')

class FileChooser(npy.NPSAppManaged):
    # def __init__(self, name='File Chooser'):
    #     self.name = name
    def onStart(self):
        self.addForm('MAIN', _FileChooserForm, name='self.name')




if __name__ == '__main__':
    app = FileChooser().run()
    pass