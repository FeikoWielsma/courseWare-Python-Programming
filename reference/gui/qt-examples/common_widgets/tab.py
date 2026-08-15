import sys
from PyQt4 import QtCore, QtGui

from ui.ui_chat import Ui_chatWindow


class ChatWindow(QtGui.QWidget, Ui_chatWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setup_ui(self)

        self.chat_view = self.chat_history_text_edit


        self.conv_tab.clear()
        self.conv_tab.set_document_mode(True)

        self.conv_tab.current_changed.connect(self.current_tab_changed)
        self.conv_tab.tab_bar().tab_close_requested.connect(self.tab_close_requested)

    def add_tab(self, contact_uri):
        if self.is_hidden():
            self.show()

        if contact_uri == '10000':
            label = "sys info"
        else:
            label = contact_uri

        chat_input = QtGui.QTextEdit()
        new_idx = self.conv_tab.add_tab(chat_input, QtCore.QString(label))
        self.conv_tab.set_current_index(new_idx)

        tabbar = self.conv_tab.tab_bar()
        tabbar.set_tab_data(new_idx, contact_uri)
        #self.conv_tab.tab_bar().set_tab_data(new_idx, contact_uri)
        #self.focus_on_current_chat_tab()
        self.conv_tab.set_tab_bar(tabbar)

        self.contact_name_label.set_text(label)

    def current_tab_changed(self, idx):
        print("current_tab_changed")
        print("current idx: %d" % idx)

        NO_TAB = -1
        if idx == NO_TAB:
            return

        tabbar = self.conv_tab.tab_bar()

        display_name = tabbar.tab_text(idx)
        self.contact_name_label.set_text(display_name)

        contact_uri = tabbar.tab_data(idx)
        print "type:", contact_uri
        print "contact_uri:", contact_uri.to_string()

    def tab_close_requested(self, idx):
        no_input = self.conv_tab.widget(idx).to_plain_text()
        if not no_input:
            self.conv_tab.remove_tab(idx)
        else:
            msg = "Pressing the ESC key will close this conversation. <br />" \
                    "Are you sure you want to continue ?"
            if popup_confirm(self, msg):
                self.conv_tab.remove_tab(idx)

        if not self.conv_tab.count():
            self.hide()

    def _close_current_tab(self):
        self.conv_tab.remove_tab(self.conv_tab.current_index())
        if not self.conv_tab.count():
            self.hide()

    def go_to_tab_by_uri(self, contact_uri):
        for idx in xrange(self.conv_tab.count()):
            tab_uri = str(self.conv_tab.tab_bar().tab_data(idx).to_string())
            if tab_uri == contact_uri:
                print("go to existed chat tab")
                self.conv_tab.set_current_index(idx)
                self.focus_on_current_chat_tab()
                return True
        return False


    def key_press_event(self, event):
        key = event.key()
        is_goto_prev_tab = (event.modifiers() == QtCore.Qt.ControlModifier) and (key == QtCore.Qt.Key_BracketLeft)
        is_goto_next_tab = (event.modifiers() == QtCore.Qt.ControlModifier) and (key == QtCore.Qt.Key_BracketRight)
        is_send_msg = key == QtCore.Qt.Key_Return
        is_close_tab = key == QtCore.Qt.Key_Escape
        is_switch_tab = (event.modifiers() == QtCore.Qt.ControlModifier) and (key >= QtCore.Qt.Key_1 and key <= QtCore.Qt.Key_9)
        CHAR_START_AT = 48

        if is_close_tab:
            if not self.conv_tab.count():
                self.hide()
                return

            no_input = self.conv_tab.current_widget().to_plain_text()
            if not no_input:
                self._close_current_tab()
            else:
                msg = "Pressing the ESC key will close this conversation. <br />" \
                        "Are you sure you want to continue ?"
                if popup_confirm(self, msg):
                    self._close_current_tab()

        elif is_send_msg:
            widget = self.conv_tab.current_widget()
            if not widget:
                return
            msg = widget.to_plain_text()
            if not msg:
                return
            widget.clear()
            print 'send'

        elif is_switch_tab:
            count = self.conv_tab.count()
            k = key.real - CHAR_START_AT
            if 1 > k and k > 9:
                return
            if k < count + 1:
                self.conv_tab.set_current_index(k - 1)
        elif is_goto_prev_tab:
            count = self.conv_tab.count()
            cur_idx = self.conv_tab.current_index()

            if count == 1:
                return
            elif cur_idx == 0:
                self.conv_tab.set_current_index(count - 1)
            else:
                self.conv_tab.set_current_index(cur_idx - 1)
        elif is_goto_next_tab:
            count = self.conv_tab.count()
            cur_idx = self.conv_tab.current_index()

            if count == 1:
                return
            elif (count - 1) == cur_idx:
                self.conv_tab.set_current_index(0)
            else:
                self.conv_tab.set_current_index(cur_idx + 1)

class Main(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self, parent = None)
        
        x, y, w, h = 500, 200, 300, 400
        self.set_geometry(x, y, w, h)

        self.chat_win = ChatWindow()

        self.chat_win.show()

        self.btn = QtGui.QPushButton(self)
        self.btn.clicked.connect(self.show_tab)

        self.add_btn = QtGui.QPushButton('add', self)
        self.add_btn.clicked.connect(self.add_tab)

        self.del_btn = QtGui.QPushButton('del', self)
        self.del_btn.clicked.connect(self.del_tab)

        qh = QtGui.QHBoxLayout()
        qh.add_widget(self.btn)
        qh.add_widget(self.add_btn)
        qh.add_widget(self.del_btn)

        self.set_layout(qh)

        self.show()

        self.c = 1

    def add_tab(self):

        self.chat_win.add_tab(str(self.c))

        self.c += 1
        
    def del_tab(self):
        pass

    def show_tab(self):
        self.chat_win.show()


def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    