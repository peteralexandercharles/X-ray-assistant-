#!/usr/bin/env python3
# -*- coding: windows-1252 -*-

# ---------------------------------------------------------------------------
# Anterior lateral and posterior osteophytes in multiple vertebral bodies.
# if "radio" or "ulna" in name_anat:
# Projection of radiopaque material in the middle zone of the right and left lung pleuro fields, (electrodes for ECG) partially compromising analysis of the radiography.
# Improve the description of the findings in the lung fields
# Fracture of the radio styloid process without joint deviation or extension.
# Fracture of the 5th metacarpal without deviation in its proximal third.
# 5th metacarpal fracture without deviation in its proximal third.
# Left costophrenic section with impaired evaluation.
# Free right costodiaphragmatic recess. >>>> Free right costodiaphragmatic recess.
# see hsdl hand
# Prominent lateral intercondylar tubercle.
# teniase in the muscle https://www.spmi.pt/22congresso/resumos_aceites_consulta.php?id=IMI-02-024
# Costophrenic breasts with impaired evaluation.
# Important accentuation of the vasobronchial web in the right lung. Acahdo may be related to infectious/inflammatory process. Correlate to clinical data.
# Important accentuation of the bilateral vasobronchial network, especially has left lung, finding may be
# Fix the reduction of joint space in the fingers
# Left lung hilum unchanged.
# Accentuation of the bilateral vasobronchial web.
# Put medical material for the lungs
# Important accentuation of the bilateral vasobronchial web.
# touch DPC in the lungs
# knee surface patellar
# Accentuation of the bilateral vasobronchial web.
# Accentuated calcification of the interspinal ligament.
# Complete fracture of the ulna styloid process, without significant bone misalignment.
# 142 patella angle.
# Hypoplastic right frontal section.
# Front breasts with usual pneumatization for the age group.
# Asymmetry of the longitudinal axis of the lumbar spine with concavity to the right.
# Double J catheter is observed in topography of the left ureter.
# Add selected location : Heterogeneity of the trabeculate...
# "diffuse"] : ex diffuse error of the ...
# I stopped at DX Fraiburgo Antonio Aparecido dos santos
#
# Entesophyte on the left iliac wing.
# Heterogeneous opacity in the right lung and lower third of the left lung, which may correspond to a pneumonic process.
# Increased cardiothoracic index.
# Elongated thoracic aorta, with tortuous, ectasitic path.
# Elongated thoracic aorta, with tortuous, ectasitic tract and atheromatous calcifications.
# Complete fracture in 5th and 6th posterior costal arch with bone misalignment.
# Wiberg's angle of approximately 30º to the left. put info
# RIGHT LAME-FEMORAL RX
# Reduction of vertebral body height of C1, possibly secondary to the bill.
# Linear opacity observed in the middle zone of the left and right lung may correspond to atelectasis.
# Chondrocostal ossifications observed.
# Reduction of disc spaces in L1-L2, L2-L3, L4-L5 and L5-S1 associated with marginal osteophytes and irregularity of vertebral plateaus.
# dlg_choose_text.Destroy() in the rest.
# delete all self.to_replace
# no net to speak to text msg self.panel_text.text_editor.WriteText(text_spoken)
# TypeError: TextEntry.WriteText(): argument 1 has unexpected type 'NoneType'
# study Ferguson Angle of 48º, value points to accentuation of physiological lumbar curvature.
# RIGHT SHOULDER RX WITH INTERNAL AND EXTERNAL ROTATION
# Incipient marginal osteophytes in multiple vertebral bodies.
# Creating a self len
# Notes and presence of venous catheter in the topography of the antecubital fossa.
#
# Place the pony fractures
# Screwed metal fixation plate, with 5 screws, in distal fibula extending to the lateral malleolus.
# At clinical criterion complementary study by comupadorized tomography could bring greater diagnostic subsidies.
# Marginal osteophyte in the upper margin of the patella.
# See and place concave foot and angles
# Cranial displacement of the anterior fat pad ('Candle Sign')
# Presence of circular radiopacity in cardiac topography, which may correspond to valve prosthesis.
# == for the system code.
# Presence of endotracheal tube positioned approximately --cm from the carina. remove
# fractures eponym
# Scanometry can have the numbers
# Angle of the trochlear groove of 126º to the right and 121º to the left, values within normality.
# Screwed metal fixation plate, with 5 screws, in the distal third of the ulna, an intact aspect and without sign of loosening. of the ulna
#
# Check text to speak for comma, period, etc.
# Verify text-to-speech operation is stopping and not coming back. see pq.

# ---------------------------------------------------------------------------
# Radiopaque, oval image, projected on soft tissues adjacent to the fibula head > adjacent to the head
# Radiological evolution control study shows knee arthroplasty, fixed on the distal third of the femur and on the proximal third of the tibia, full prosthesis and no signs of loosening. > knee arthroplasty.
# , ACHDO etc, > in undesirable upper
# Obliteration of the suprapatellar fat pad > and infra
# An extensive lytic, centric lesion is observed in the calcaneus that inflates the cortical, with defined contours, short transition zone, with adjacent halo of sclerosis and intralesional fibrous beams, compatible with simple bone cyst. > not well described
# Osteophytes in the tibial plateau, femoral condyles and posterior edges of the patella. > placing insipients
# Obliteration of the suprapatellar fat pad, which may correspond to joint effusion. Obliteration of the suprapatellar fat pad | may correspond to joint effusion.
#
# check a method for oit torax reporting
# put explanation for e.g.: spoken_text = spoken_text.replace(" End point", ".".
# put lamp for additional continuing medical education content

# -------------------------- SYSTEM UPDATE --------------------------
#
# cololar to install in the folder C:\Cosmo Radiology
# Review license terms and information
# Update too much in anatomy and txt


"""Interactive assistant to perform reports of
x-ray."""

import wx
import sys
import anatomy as anat
import info_paciente_widget as info_pw
import speech_recognition as sr
import _thread as thread
import template_txt as temp_txt
import json
from urllib.request import urlopen
import wx.adv

# ID Módulos
from uuid import getnode as get_mac

# -=-=-=-=-=-=-=---=-=-=- Presentation -=-=-=-=-=-=-=-=-=-=-=-=

class MyPanel_Apresentacao(wx.Panel):
    """Stylized presentation"""

    def __init__(self, parent, link=True, img_name="xrd135_2.png", url_web="https://www.peteralexandercharles.com/",
                 url_label="                              https://www.peteralexandercharles.com/                              "):
        """Builder"""
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.on_eraseBackground)
        self.img_name = img_name

        if link == True:
            space = "                              "
            label_txt = url_label
            url_link = wx.adv.HyperlinkCtrl(self, -1, label=label_txt, url=url_web,
                                            pos=(25, 510), size=(1000, 50),style=wx.adv.HL_ALIGN_CENTRE)
            fonte = wx.Font(wx.FontInfo(20))
            url_link.SetFont(fonte)
            url_link.SetBackgroundColour("white")


    def on_eraseBackground(self, event):
        """Clean correlate with the past medical history to place image"""
        dc = event.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRegion(rect)
        dc.Clear()

        # logo Cosmo
        bmp = wx.Image(self.img_name, wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        dc.DrawBitmap(bmp, 0, 0)



class MyFrame_Apresentacao(wx.Frame):
    """Presentation window"""
    def __init__(self, parent, style=wx.DEFAULT_FRAME_STYLE, link=True, img_name = "xrd135_2.png", url="https://www.peteralexandercharles.com/", url_label="                              https://www.peteralexandercharles.com/                              "):
        """Construtor"""
        wx.Frame.__init__(self, parent=parent, size=(1030, 600), style=style)
        self.panel = MyPanel_Apresentacao(self, link=link, img_name=img_name, url_web=url, url_label=url_label)
        self.url = url
        ico = wx.Icon("xrd136.ico")
        self.SetIcon(ico)
        self.Bind(wx.adv.EVT_HYPERLINK, self.on_click)
        self.Center()
        self.Show()

    def on_click(self, event):
        """Close by clicking on the link"""
        print("IR")
        wx.LaunchDefaultBrowser(self.url)
        self.Close()


# -=-=-=-=-=-=-=-=- Frame check user -=-=-=-=-=-=-=-=-=-=-=-=-=-

class MyFileDropTarget(wx.FileDropTarget):
    """Drag and Drop class initializing
    attributes of the child class."""
    def __init__(self, target):
        """Initialize class attributes
        inherits from wx.FileDropTarget"""
        super(MyFileDropTarget, self).__init__()
        self.target = target

    def OnDropFiles(self, x, y, filenames):
        for fname in filenames:
            self.target.SetValue("")
            self.target.WriteText(fname)


class MyPanel_Key(wx.Panel):
    """Panel for frame key"""
    def __init__(self, parent):
        """Function to initialize the
        class attributes."""
        super(MyPanel_Key, self).__init__(parent)

        # Layout Gerenciar
        vSizer = wx.BoxSizer(wx.VERTICAL)
        hSizer1 = wx.BoxSizer(wx.HORIZONTAL)



        # Label
        self.label_id = wx.StaticText(self, label="My ID:")
        hSizer1.Add(self.label_id, 0, wx.ALL|wx.ALIGN_CENTER, 5)

        id_img = wx.Image("xrd141.ipn").ConvertToBitmap()
        id_static_bitmap = wx.StaticBitmap(self, -1, bitmap=id_img)
        hSizer1.Add(id_static_bitmap, 0, wx.ALL|wx.ALIGN_CENTER, 5)

        # Text Ctrl
        self.text_ctrl_id = wx.TextCtrl(self, style=wx.TE_READONLY)
        hSizer1.Add(self.text_ctrl_id, 1, wx.ALL|wx.ALIGN_CENTER, 5)
        vSizer.Add(hSizer1, 1, wx.EXPAND)

        key_img = wx.Image("donation_icon.png").ConvertToBitmap()
        key_static_bitmap = wx.StaticBitmap(self, -1, bitmap=key_img, pos=(40, 150))

        # Linha 2
        hSizer2 = wx.BoxSizer()

        self.label_key_code = wx.StaticText(self, label="My Activation Key:")
        hSizer2.Add(self.label_key_code, 0, wx.ALL|wx.TOP, 5)

        self.text_ctrl_lisence = wx.TextCtrl(self, style=wx.TE_READONLY|wx.TE_MULTILINE)
        hSizer2.Add(self.text_ctrl_lisence, 1, wx.ALL|wx.EXPAND, 5)
        vSizer.Add(hSizer2, 1, wx.EXPAND)

        # Linha 3
        hSizer3 = wx.BoxSizer()

        # Btn OK
        self.ok_btn = wx.Button(self, wx.ID_OK, label="OK")
        ok_bitmap = wx.Image("xrd112.png").ConvertToBitmap()
        self.ok_btn.SetBitmap(ok_bitmap)
        hSizer3.Add(self.ok_btn, 1, wx.ALL|wx.ALIGN_CENTER, 5)

        # Btn Cancel
        self.cancel_btn = wx.Button(self, wx.ID_CANCEL, label="Cancel")
        cancel_bitmap = wx.Image("xrd125.ipn").ConvertToBitmap()
        self.cancel_btn.SetBitmap(cancel_bitmap)

        hSizer3.Add(self.cancel_btn, 1, wx.ALL|wx.ALIGN_CENTER, 5)
        vSizer.Add(hSizer3, 1, wx.EXPAND)

        # Linha 4
        hSizer4 = wx.BoxSizer()

        # CommandLink Button
        note = """To activate your license just drag it to this window.
In case you don't have your license yet, please call us at (41) 98444-9186,
quick service through Whatsapp or our website: https://www.peteralexandercharles.com/
Click Here to be directed to our webpage."""
        self.cml_btn = wx.adv.CommandLinkButton(self, mainLabel="Just Drag and Drop Your Key in That Window!",
                                                note=note)
        hSizer4.Add(self.cml_btn, 1, wx.EXPAND)
        vSizer.Add(hSizer4, 1, wx.EXPAND)

        # SetSizer
        self.SetSizer(vSizer)
        self.SetInitialSize()

class MyFrame_Key(wx.Frame):
    """Frame"""
    def __init__(self, parent, title="Activation Key", destroi_parent=False):
        """Frame Class, Constructor"""
        super(MyFrame_Key, self).__init__(parent, title=title,
                                          style=wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT)

        self.destroi_parent = destroi_parent
        self.parent = parent

        # Set Icon
        ico = wx.Icon("xrd138.iico")
        self.SetIcon(ico)
        size_frame = (600, 450)
        self.SetMinClientSize(size_frame)
        self.SetMaxClientSize(size_frame)

        # Panel
        self.panel = MyPanel_Key(self)

        # Drag and Drop Power for the whole Frame
        dropTarget = MyFileDropTarget(self.panel.text_ctrl_lisence)
        self.panel.SetDropTarget(dropTarget)

        # Show
        self.Show()

        # Bind
        self.Bind(wx.EVT_BUTTON, self.on_cancel_btn, self.panel.cancel_btn)
        self.Bind(wx.EVT_BUTTON, self.on_cml_btn, self.panel.cml_btn)
        self.Bind(wx.EVT_BUTTON, self.on_ok_btn, self.panel.ok_btn)
        self.Bind(wx.EVT_CLOSE, self.on_close)

        # Functions of Frame_Key

        # Builder function
        self.on_meu_id_code()

    def on_close(self, event):
        """Close"""
        if self.destroi_parent == True:
            self.parent.Close()
        else:
            self.Destroy()

    def on_meu_id_code(self):
        """Put id in TextCtrl"""
        meu_id_int = get_mac()
        meu_id_str = str(meu_id_int)
        app_id_f = "RX-"
        meu_id_str = app_id_f + meu_id_str.replace("0", "QA").replace("1", "WS").replace("2", "ED").replace("3", "RF")\
            .replace("4", "TG").replace("5", "YH")
        self.panel.text_ctrl_id.SetValue(meu_id_str)

    def on_cancel_btn(self, event):
        """By clicking cancel close"""
        self.Close()
        if self.destroi_parent == True:
            self.parent.Close()

    def on_cml_btn(self, event):
        """By clicking CML be directed
        to the website."""
        site = "https://https://www.peteralexandercharles.com/"
        ir_ao_site = wx.LaunchDefaultBrowser(site)

    def on_ok_btn(self, event):
        """By clicking the ok button pick
        data for validation."""
        print("Getting data for validation")
        filename = self.panel.text_ctrl_lisence.GetValue()
        print(filename)

        try:
            with open(filename, "r") as fileobject:
                texto_do_file = json.load(fileobject)
                for key in texto_do_file.keys():
                    key_cosmo_atual = key
                print("Key Cosmo Atual:", key_cosmo_atual)

        except FileNotFoundError:
            pass

        except UnicodeDecodeError:
            msg = wx.MessageBox("It was not possible to validate your license, check if it is the validation key provided!",
                                "Invalid file", wx.ICON_INFORMATION)
            self.Close()
        except:
            print("Error when validating strange file!")
            msg = wx.MessageBox("It was not possible to validate.\nCheck if it is the validation key provided!",
                                "Invalid file", wx.ICON_INFORMATION)
            self.Close()

        else:
            app_id = "RX"
            try:
                mac_da_key_str = key_cosmo_atual.split(app_id, 1)[1]
            except IndexError:
                print("Arquivo invalido! msgid=111")
                msg_validada = wx.MessageBox(
                    "Invalid file!\n\nMake sure you have provided the correct key or contact Cosmo Radiology at WhatsApp (41)98444-9186 for a quick reply!\nWe quickly released a free license for you to test our Assistant!\n\nWebsite: https://www.peteralexandercharles.com/",
                    "Invalid file!",
                    parent=self)
            else:
                mac_da_key_int = int(mac_da_key_str)
                pc_id = get_mac()

                if mac_da_key_int == pc_id:
                    print("ID valido!")

                    with open("xrd81.ipn", "r") as fileobject:
                        date_id_pc = fileobject.read()
                        print(date_id_pc)
                    with open("xrd81.ipn", "w") as fileobject:
                        json.dump(texto_do_file, fileobject)
                        print("json.dump:", texto_do_file)

                    msg_sucesso = wx.MessageBox("Congratulations, your license has been successfully validated!!!\n"
                                                "We wish you great reports!",
                                                "License validated!", style=wx.ICON_INFORMATION)

                else:
                    print("ID invalid!")
                    msg_validada = wx.MessageBox(
                        "License already in use!\n\nContact Cosmo Radiology at WhatsApp (41)98444-9186 for a quick reply!",
                        "ID já em uso",
                        parent=self)

                # Now you decide when to close
                self.Close()
                if self.destroi_parent == True:
                    self.parent.Close()


# -=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-= Customer Templates -=-=-=-=-=-=-=-=-=-=-=-

class PanelParaCodigos_Template(wx.Panel):
    """Panel to hold the widgets of the
    FrameForCodes."""
    def __init__(self, parent):
        """Initialize the child's atrubuto."""
        super(PanelParaCodigos_Template, self).__init__(parent)

        vSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vSizer)

        hSizer1 = wx.BoxSizer()
        vSizer.Add(hSizer1, 1, wx.EXPAND)

        codito_label = wx.StaticText(self, -1, "Standard:")
        hSizer1.Add(codito_label, 0, wx.ALL|wx.CENTER, 5)
        self.text_codigo = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE|wx.TE_READONLY)
        self.text_codigo.SetBackgroundColour(wx.NullColour)
        hSizer1.Add(self.text_codigo, 1, wx.LEFT|wx.EXPAND, 40)

        hSizer2 = wx.BoxSizer()
        vSizer.Add(hSizer2, 0, wx.EXPAND)
        img_btn_down = wx.Image("xrd121.ipn").ConvertToBitmap()
        self.btn_down = wx.BitmapButton(self, -1, bitmap=img_btn_down)
        hSizer2.Add(self.btn_down, 1, wx.CENTER)

        hSizer3 = wx.BoxSizer()
        vSizer.Add(hSizer3, 1, wx.EXPAND)
        texto_label = wx.StaticText(self, -1, "Customize:")
        hSizer3.Add(texto_label, 0, wx.ALL|wx.CENTER, 5)
        self.text_ass_ao_codigo = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        hSizer3.Add(self.text_ass_ao_codigo, 1, wx.LEFT|wx.EXPAND, 5)

        hSizer4 = wx.BoxSizer()
        vSizer.Add(hSizer4, 0, wx.EXPAND)
        self.btn_OK = wx.Button(self, wx.ID_OK)
        img_btn_ok = wx.Image("xrd112.png").ConvertToBitmap()
        self.btn_OK.SetBitmap(img_btn_ok)
        hSizer4.Add(self.btn_OK, 1, wx.ALL|wx.ALIGN_CENTER, 5)

        self.btn_Cancel = wx.Button(self, wx.ID_CANCEL)
        img_btn_cancel = wx.Image("xrd125.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.btn_Cancel.SetBitmap(img_btn_cancel)
        hSizer4.Add(self.btn_Cancel, 1, wx.ALL|wx.ALIGN_CENTER, 5)


class FrameParaCodigos_Template(wx.Frame):
    """Frame to receive from the user the codes of
    custom temple."""
    def __init__(self, parent, title="Customize your templates", text="", memo_file=""):
        """Initialize child attributes."""
        super(FrameParaCodigos_Template, self).__init__(parent, title=title,
       style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)

        self.filename = memo_file
        self.Center()

        # Definir tamanho da janela
        self.SetSize(600, 500)

        # Gerenciador de Layout Horizontal
        self.hSizer = wx.BoxSizer()
        # Gerenciador de Layout Vertical
        self.vSizer = wx.BoxSizer(wx.VERTICAL)
        self.vSizer.Add(self.hSizer, 1, wx.EXPAND)
        self.SetSizer(self.vSizer)

        ico = wx.Icon("xrd123.ipn")
        self.SetIcon(ico)

        self.panel = PanelParaCodigos_Template(self)
        self.vSizer.Add(self.panel, 1, wx.EXPAND)
        self.panel.text_codigo.SetValue(text)
        self.text = text

        self.Show()

        self.Bind(wx.EVT_BUTTON, self.on_btn_down, self.panel.btn_down)
        self.Bind(wx.EVT_BUTTON, self.on_btn_cancel, self.panel.btn_Cancel)
        self.Bind(wx.EVT_BUTTON, self.on_btn_ok, self.panel.btn_OK)

        if text == "":
            self.panel.Disable()

    def on_btn_down(self, event):
        """By clicking on Bitmapbutton down
        copy text from pattern to custom
        thus facilitating the desired change."""
        self.panel.text_ass_ao_codigo.SetValue("")
        self.panel.text_ass_ao_codigo.SetValue(self.text)

    def on_btn_cancel(self, event):
        """By clicking the cancel button
        if you destroy."""
        print("Destroy code window.")
        self.Destroy()

    def on_btn_ok(self, event):
        """By clicking the ok button
        ready to save the text-code pair
        of the user."""
        print("Ready to save the text-code pair!")
        codigo = self.panel.text_codigo.GetValue()
        codigo = codigo.replace("==", "").strip()
        texto = self.panel.text_ass_ao_codigo.GetValue()
        texto = texto.strip()
        print("Code: {} Text: {}".format(codigo, texto))
        filename = self.filename

        with open(filename, "r") as file_object:
            lista_pega = json.load(file_object)
            dic_formado = {}

            for dic in lista_pega:
                print("Here dictionary", dic)
                for key, value in dic.items():
                    dic_formado[key] = value
                    if codigo == key:
                        print("Equal")
                        if codigo != "":
                            dic_formado[key] = value

        if codigo != "":
            with open(filename, "w") as file_object:
                dic_code = {}
                dic_code[codigo] = texto
                dic_formado[codigo] = texto
                lista_pega = []
                lista_pega.append(dic_formado)
                json.dump(lista_pega, file_object)
            self.Close()
            self.Destroy()

# --=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Label-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class PanelParaCodigos_Texto(wx.Panel):
    """Panel to hold the widgets of the
    FrameForCodes."""
    def __init__(self, parent):
        """Initialize the child's atrubuto."""
        super(PanelParaCodigos_Texto, self).__init__(parent)

        vSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vSizer)

        hSizer1 = wx.BoxSizer()
        vSizer.Add(hSizer1, 1, wx.EXPAND)

        codito_label = wx.StaticText(self, -1, "Standard:")
        hSizer1.Add(codito_label, 0, wx.ALL|wx.CENTER, 5)
        self.text_codigo = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE|wx.TE_READONLY)
        hSizer1.Add(self.text_codigo, 1, wx.LEFT|wx.EXPAND, 40)

        hSizer2 = wx.BoxSizer()
        vSizer.Add(hSizer2, 0, wx.EXPAND)
        img_btn_down = wx.Image("xrd121.ipn").ConvertToBitmap()
        self.btn_down = wx.BitmapButton(self, -1, bitmap=img_btn_down)
        hSizer2.Add(self.btn_down, 1, wx.CENTER)

        hSizer3 = wx.BoxSizer()
        vSizer.Add(hSizer3, 1, wx.EXPAND)
        texto_label = wx.StaticText(self, -1, "Customize:")
        hSizer3.Add(texto_label, 0, wx.ALL|wx.CENTER, 5)
        self.text_ass_ao_codigo = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        hSizer3.Add(self.text_ass_ao_codigo, 1, wx.LEFT|wx.EXPAND, 5)

        hSizer4 = wx.BoxSizer()
        vSizer.Add(hSizer4, 0, wx.EXPAND)
        self.btn_OK = wx.Button(self, wx.ID_OK)
        img_btn_ok = wx.Image("xrd112.png").ConvertToBitmap()
        self.btn_OK.SetBitmap(img_btn_ok)
        hSizer4.Add(self.btn_OK, 1, wx.ALL|wx.ALIGN_CENTER, 5)

        self.btn_Cancel = wx.Button(self, wx.ID_CANCEL)
        img_btn_cancel = wx.Image("xrd125.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.btn_Cancel.SetBitmap(img_btn_cancel)
        hSizer4.Add(self.btn_Cancel, 1, wx.ALL|wx.ALIGN_CENTER, 5)


class FrameParaCodigos_Texto(wx.Frame):
    """Frame to receive from the user the codes of
    custom temple."""
    def __init__(self, parent, title="Codes for text", text="", memo_file=""):
        """Initialize child attributes."""
        super(FrameParaCodigos_Texto, self).__init__(parent, title=title,
       style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)

        self.filename = memo_file
        self.Center()

        # Set window size
        self.SetSize(600, 500)

        # Horizontal Layout Manager
        self.hSizer = wx.BoxSizer()
        # Vertical Layout Manager
        self.vSizer = wx.BoxSizer(wx.VERTICAL)
        self.vSizer.Add(self.hSizer, 1, wx.EXPAND)
        self.SetSizer(self.vSizer)

        ico = wx.Icon("xrd123.ipn")
        self.SetIcon(ico)

        self.panel = PanelParaCodigos_Texto(self)
        self.vSizer.Add(self.panel, 1, wx.EXPAND)
        self.panel.text_codigo.SetValue(text)
        self.text = text

        self.Show()

        self.Bind(wx.EVT_BUTTON, self.on_btn_down, self.panel.btn_down)
        self.Bind(wx.EVT_BUTTON, self.on_btn_cancel, self.panel.btn_Cancel)
        self.Bind(wx.EVT_BUTTON, self.on_btn_ok, self.panel.btn_OK)

        if text == "":
            self.panel.Disable()

    def on_btn_down(self, event):
        """By clicking on Bitmapbutton down
         copy text from standard to custom
         thus facilitating the desired change."""
        self.panel.text_ass_ao_codigo.SetValue("")
        self.panel.text_ass_ao_codigo.SetValue(self.text)

    def on_btn_cancel(self, event):
        """By clicking the button cancel
         destroy itself."""
        print("Destroy code window.")
        self.Destroy()

    def on_btn_ok(self, event):
        """By clicking the ok button
         ready to save the code-text pair
         of user."""
        print("Ready to save the code-text pair!")
        codigo = self.panel.text_codigo.GetValue()
        codigo = codigo.replace("==", "").strip()
        texto = self.panel.text_ass_ao_codigo.GetValue()
        texto = texto.strip()
        print("Code: {} Text: {}".format(codigo, texto))
        filename = self.filename

        try:
            with open(filename, "r") as file_object:
                lista_pega = json.load(file_object)
                dic_formado = {}

                for dic in lista_pega:
                    print("Here Dictionary", dic)
                    for key, value in dic.items():
                        dic_formado[key] = value
                        if codigo == key:
                            print("Equal")
                            if codigo != "":
                                dic_formado[key] = value
        except FileNotFoundError:
            dic_formado = {}
            dic_formado["rx123"] = "memo dic custom phrase created"

        if codigo != "":
            with open(filename, "w") as file_object:
                dic_code = {}
                dic_code[codigo] = texto
                dic_formado[codigo] = texto
                lista_pega = []
                lista_pega.append(dic_formado)
                json.dump(lista_pega, file_object)
            self.Close()
            self.Destroy()

# ------------------------------------------------------------------------

class PanelParaCodigos(wx.Panel):
    """Panel para segurar os widgets da
    Frame FrameParaCodigos."""
    def __init__(self, parent):
        """Inicializar atrubutos do filho."""
        super(PanelParaCodigos, self).__init__(parent)

        vSizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vSizer)

        hSizer1 = wx.BoxSizer()
        vSizer.Add(hSizer1, 0, wx.EXPAND)

        codito_label = wx.StaticText(self, -1, "Código:")
        hSizer1.Add(codito_label, 0, wx.ALL|wx.CENTER, 5)
        self.text_codigo = wx.TextCtrl(self, -1)
        hSizer1.Add(self.text_codigo, 1, wx.ALL, 10)

        hSizer2 = wx.BoxSizer()
        vSizer.Add(hSizer2, 1, wx.EXPAND)
        texto_label = wx.StaticText(self, -1, "Texto:")
        hSizer2.Add(texto_label, 0, wx.ALL, 5)
        self.text_ass_ao_codigo = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        hSizer2.Add(self.text_ass_ao_codigo, 1, wx.ALL|wx.EXPAND, 10)

        hSizer3 = wx.BoxSizer()
        vSizer.Add(hSizer3, 0, wx.EXPAND)
        self.btn_OK = wx.Button(self, wx.ID_OK)
        img_btn_ok = wx.Image("xrd112.png").ConvertToBitmap()
        self.btn_OK.SetBitmap(img_btn_ok)
        hSizer3.Add(self.btn_OK, 1, wx.ALL|wx.ALIGN_CENTER, 5)

        self.btn_Cancel = wx.Button(self, wx.ID_CANCEL)
        img_btn_cancel = wx.Image("xrd125.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.btn_Cancel.SetBitmap(img_btn_cancel)
        hSizer3.Add(self.btn_Cancel, 1, wx.ALL|wx.ALIGN_CENTER, 5)


class FrameParaCodigos(wx.Frame):
    """Quadro para receber do usuário os códigos de
    personalizados de templetes."""
    def __init__(self, parent, title="Códigos para texto"):
        """Inicializar atributos do filho."""
        super(FrameParaCodigos, self).__init__(parent, title=title,
       style=wx.FRAME_FLOAT_ON_PARENT|wx.DEFAULT_FRAME_STYLE)

        self.Center()

        # Gerenciador de Layout Horizontal
        self.hSizer = wx.BoxSizer()
        # Gerenciador de Layout Vertical
        self.vSizer = wx.BoxSizer(wx.VERTICAL)
        self.vSizer.Add(self.hSizer, 1, wx.EXPAND)
        self.SetSizer(self.vSizer)

        ico = wx.Icon("xrd123.ipn")
        self.SetIcon(ico)

        self.panel = PanelParaCodigos(self)
        self.vSizer.Add(self.panel, 1, wx.EXPAND)

        self.Show()

        self.Bind(wx.EVT_BUTTON, self.on_btn_cancel, self.panel.btn_Cancel)
        self.Bind(wx.EVT_BUTTON, self.on_btn_ok, self.panel.btn_OK)

    def on_btn_cancel(self, event):
        """Ao clicar no button cancel
        se destruir."""
        print("Destruir janela de código.")
        self.Destroy()

    def on_btn_ok(self, event):
        """Ao clicar no button ok
        pronto para salvar o par código-texto
        do usuário."""
        print("Pronto para salvar o par código-texto!")
        codigo = self.panel.text_codigo.GetValue()
        codigo = codigo.replace("==", "").strip()
        texto = self.panel.text_ass_ao_codigo.GetValue()
        texto = texto.strip()
        print("Código: {} Texto: {}".format(codigo, texto))
        filename = "xrd79.ipn"

        try:
            with open(filename, "r") as file_object:
                lista_pega = json.load(file_object)
                dic_formado = {}

                for dic in lista_pega:
                    print("Aqui DIc", dic)
                    for key, value in dic.items():
                        dic_formado[key] = value
                        if codigo == key:
                            print("Igual")
                            if codigo != "":
                                dic_formado[key] = value
        except FileNotFoundError:
            dic_formado = {}
            dic_formado["rx123"] = "memo dic codigo personalizado criado"

        if codigo != "":
            with open(filename, "w") as file_object:
                dic_code = {}
                dic_code[codigo] = texto
                dic_formado[codigo] = texto
                lista_pega = []
                lista_pega.append(dic_formado)
                json.dump(lista_pega, file_object)

        self.Close()
        self.Destroy()



class FalaParaTexto():
    """Classe converte texto falado em texto."""

    def get_mic(self):
        """Get mic"""
        try:
            source = sr.Microphone()
            return source
        except OSError:
            print("get mic Error: OSError")
            return None


    def audio_para_texto(self):
        """Função para reconhecer fala"""


        reconhecer = sr.Recognizer()

        with sr.Microphone() as fonte:

            print("I'm hearing!")
            # Tentativa de melhorar para lugares com barulho
            reconhecer.adjust_for_ambient_noise(source=fonte, duration=0.7)


            try:
                # Time Setup SpeechRecognition defalt timeout=5, phrase_time_limit=4
                audio = reconhecer.listen(
                    source=fonte, timeout=None, phrase_time_limit=12)
            except sr.WaitTimeoutError:
                print("speech_recognition.WaitTimeoutError")
                return
            try:
                texto_falado = reconhecer.recognize_google(
                    audio_data=audio, key=None, language="en-US", show_all=False
                )
                return str(texto_falado)
            except sr.UnknownValueError:
                print("speech_recognition.UnknowValueError")
                return
            except Exception as e:
                print("Other Exception:", e)

            except sr.UnknownValueError:
                print("I didn't understand")
            except sr.RequestError:
                print("Connection failure")
            else:
                return texto_falado


class MyTabPanel(wx.Panel):

    def __init__(self, parent):
        """Classe Notebook tab."""
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundColour("white")

class MyTabScroll(wx.ScrolledWindow):

    def __init__(self, parent):
        """Classe Notebook tab."""
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundColour("white")

class MyPanel_text_editor(wx.Panel):
    """Panel para TextCtrl."""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_text_editor, self).__init__(parent)

        # Gerenciador de Layout
        down = wx.BoxSizer(wx.VERTICAL)
        row1 = wx.BoxSizer()

        # Widget TextCtrl
        self.text_editor = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        row1.Add(self.text_editor, 1, wx.EXPAND|wx.ALL, 5)
        down.Add(row1, 1, wx.EXPAND)

        # SetSizer
        self.SetSizer(down)


class MyPanel_info_clinica(wx.Panel):
    """Panel para exibir informação relevente
    em tempo real para auxiliar nos diagnósticos."""
    def __init__(self, parent):
        """Inicializar atributos da classe"""
        super(MyPanel_info_clinica, self).__init__(parent)

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        #tab1.SetBackgroundColour("black")
        notebook.AddPage(tab1, "Informação")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.EXPAND)
        self.SetSizer(vSizer)

        # Gerenciador de layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        # Texto relevante

        self.texto_info_clinica = wx.TextCtrl(tab1, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)
        vSizer.Add(self.texto_info_clinica, 1, wx.EXPAND)

        # image dica #400X318
        self.file_img = wx.Image("xrd116.ipn").ConvertToBitmap()
        self.info_imagem = wx.StaticBitmap(tab1, -1, bitmap=self.file_img)

        vSizer.Add(self.info_imagem, 1, wx.EXPAND)
        tab1.SetSizer(vSizer)

        # TAB 2
        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Sugestão de conclusão")

        # Texto conclusão
        self.conclusao_info_clinica = wx.TextCtrl(tab2, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)
        vSizer_tab2 = wx.BoxSizer(wx.VERTICAL)
        vSizer_tab2.Add(self.conclusao_info_clinica, 1, wx.EXPAND)
        tab2.SetSizer(vSizer_tab2)


class MyPanel_img_torax(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_img_torax, self).__init__(parent)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA 1")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "PA 2")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Perfil 1")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # Rx normal
        self.btn = anat.Anatomy.rx_normal(tab1, 521, 27, 20, 20)

        # Coração
        self.btn = anat.Anatomy.heart(tab1, 350, 300, 20, 20)
        self.btn = anat.Anatomy.heart(tab2, 328, 336, 20, 20)
        self.btn = anat.Anatomy.heart(tab3, 132, 283, 20, 20)

        # Ventriculo esquerdo
        self.btn = anat.Anatomy.atrium(tab1, 376, 311, 20, 20, "left ventricle")

        # Ventriculo direito
        self.btn = anat.Anatomy.atrium(tab1, 267, 303, 20, 20, "right ventricle")


        # Atrio esquerdo
        self.btn = anat.Anatomy.atrium(tab1, 354, 244, 20, 20, "left atrium")

        # Atrio esquerdo
        self.btn = anat.Anatomy.atrium(tab1, 228, 268, 20, 20, "right atrium")

        # Aorta
        self.btn = anat.Anatomy.aorta(tab1, 311, 109, 20, 20)
        self.btn = anat.Anatomy.aorta(tab2, 316, 175, 20, 20)
        self.btn = anat.Anatomy.aorta(tab3, 256, 159, 20, 20)

        # Mediastino
        self.btn = anat.Anatomy.mediastino(tab1, 278, 211, 20, 20)
        self.btn = anat.Anatomy.mediastino(tab3, 110, 184, 20, 20)

        # Subclávia
        self.btn = anat.Anatomy.subclavia(tab1, 132, 43, 20, 20, "right subclavian")
        self.btn = anat.Anatomy.subclavia(tab1, 432, 49, 20, 20, "left subclavian")
        self.btn = anat.Anatomy.subclavia(tab2, 153, 47, 20, 20, "right subclavian")
        self.btn = anat.Anatomy.subclavia(tab2, 410, 50, 20, 20, "left subclavian")

        # Pulmão
        self.btn_anat = anat.Anatomy.lung(tab1, 131, 187, 20, 20, "right lung")
        self.btn_anat = anat.Anatomy.lung(tab1, 414, 188, 20, 20, "left lung")

        self.btn_anat = anat.Anatomy.lung(tab2, 135, 205, 20, 20, "right lung")
        self.btn_anat = anat.Anatomy.lung(tab2, 408, 208, 20, 20, "left lung")

        # Traqueia
        self.btn_anat = anat.Anatomy.traqueia(tab1, 281, 50, 20, 20)
        self.btn_anat = anat.Anatomy.traqueia(tab2, 287, 75, 20, 20)
        self.btn_anat = anat.Anatomy.traqueia(tab3, 251, 67, 20, 20)

        # Esofago
        self.btn_anat = anat.Anatomy.esofago(tab1, 283, 73, 20, 20)
        self.btn_anat = anat.Anatomy.esofago(tab3, 209, 55, 20, 20)

        # Diafragma
        self.btn_anat = anat.Anatomy.diafragma(tab1, 124, 323, 20, 20, "right hemidiaphragm")
        self.btn_anat = anat.Anatomy.diafragma(tab1, 426, 334, 20, 20, "left hemidiaphragm")
        self.btn_anat = anat.Anatomy.diafragma(tab2, 148, 422, 20, 20, "right hemidiaphragm")
        self.btn_anat = anat.Anatomy.diafragma(tab2, 430, 435, 20, 20, "left hemidiaphragm")
        self.btn_anat = anat.Anatomy.diafragma(tab3, 238, 459, 20, 20, "right hemidiaphragm")
        self.btn_anat = anat.Anatomy.diafragma(tab3, 224, 424, 20, 20, "left hemidiaphragm")

        # Hilo
        self.btn = anat.Anatomy.hilo(tab1, 200, 200, 20, 20, "hilum right")
        self.btn_1 = anat.Anatomy.hilo(tab1, 350, 165, 20, 20, "left hilum")
        self.btn = anat.Anatomy.hilo(tab2, 219, 238, 20, 20, "hilum right")
        self.btn_1 = anat.Anatomy.hilo(tab2, 348, 245, 20, 20, "left hilum")

        # costophrenic recess
        self.btn = anat.Anatomy.costodiaphragmatic_recess(tab1, 55, 355, 20, 20, "right costodiaphragmatic recess")
        self.btn = anat.Anatomy.costodiaphragmatic_recess(tab1, 501, 368, 20, 20, "left costodiaphragmatic recess")
        self.btn = anat.Anatomy.costodiaphragmatic_recess(tab2, 93, 497, 20, 20, "right costodiaphragmatic recess")
        self.btn = anat.Anatomy.costodiaphragmatic_recess(tab2, 469, 490, 20, 20, "left costodiaphragmatic recess")
        self.btn = anat.Anatomy.costodiaphragmatic_recess(tab3, 35, 393, 20, 20, "anterior costophrenic angle seen on the radiograph in profile")
        self.btn = anat.Anatomy.costodiaphragmatic_recess(tab3, 299, 470, 20, 20, "posterior costophrenic angle of the left diaphragmatic hemicome")
        self.btn = anat.Anatomy.costodiaphragmatic_recess(tab3, 274, 537, 20, 20, "posterior costophrenic angle of the right diaphragmatic hemicome")

        # Escapula
        self.btn = anat.Anatomy.osso_generico(tab1, 55, 99, 20, 20, "right scapula", "")
        self.btn = anat.Anatomy.osso_generico(tab1, 493, 98, 20, 20, "left scapula", "")

        self.btn = anat.Anatomy.osso_generico(tab2, 77, 121, 20, 20, "right scapula", "")
        self.btn = anat.Anatomy.osso_generico(tab2, 489, 135, 20, 20, "left scapula", "")

        # Esterno
        self.btn = anat.Anatomy.osso_generico(tab1, 274, 183, 20, 20, "sternum", "")
        self.btn = anat.Anatomy.osso_generico(tab3, 71, 183, 20, 20, "sternum", "")

        # Clavícula
        self.btn = anat.Anatomy.osso_generico(tab1, 128, 12, 20, 20, "right collarbone")
        self.btn = anat.Anatomy.osso_generico(tab1, 434, 29, 20, 20, "left collarbone")

        # costela
        self.btn = anat.Anatomy.osso_generico(tab1, 66, 208, 20, 20, "1st right rib")
        self.btn = anat.Anatomy.osso_generico(tab1, 488, 203, 20, 20, "2nd left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 96, 246, 20, 20, "1st right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 460, 252, 20, 20, "2nd left rib")

        # coluna torácica
        self.btn = anat.Anatomy.coluna_toracica(tab3, 311, 202, 20, 20, "thoracic spine")

        # mama
        self.btn = anat.Anatomy.mama(tab1, 52, 405, 20, 20, "right breast")
        self.btn = anat.Anatomy.mama(tab1, 505, 415, 20, 20, "left breast")

        # parte mole
        self.btn = anat.Anatomy.parte_mole(tab1, 0, 196, 20, 20, "soft part of the right arm")
        self.btn = anat.Anatomy.parte_mole(tab1, 543, 207, 20, 20, "soft part of the left arm")

        # Imagem tap 1 PA Tórax
        torax_img_pa1 = wx.Image("xrd1-1.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab1, bitmap=torax_img_pa1, pos=wx.DefaultPosition)

        # Imagem tap 2 PA Tórax Ossos
        torax_img_pa2 = wx.Image("xrd2-2.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab2, bitmap=torax_img_pa2, pos=(60, -1))

        # Imagem tap 2 Perfil Tórax
        torax_img_perfil1 = wx.Image("xrd3-3.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab3, bitmap=torax_img_perfil1, pos=wx.DefaultPosition)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class MyPanel_img_coluna_cervical(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_img_coluna_cervical, self).__init__(parent)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA 1")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Lateral")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Atlas C1")

        tab4 = MyTabPanel(notebook)
        notebook.AddPage(tab4, "C1-C2")


        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # C1
        self.btn = anat.Anatomy.vertebra(tab2, 164, 119, 20, 20, "C1")
        self.btn = anat.Anatomy.vertebra(tab3, 179, 223, 20, 20, "C1")

        self.btn = anat.Anatomy.osso_generico(tab4, 133, 83, 20, 20, "odontoid process")
        self.btn = anat.Anatomy.osso_generico(tab4, 426, 90, 20, 20, "odontoid process")

        self.btn = anat.Anatomy.osso_generico(tab4, 48, 147, 20, 20, "C2 right lateral region")
        self.btn = anat.Anatomy.osso_generico(tab4, 208, 147, 20, 20, "left lateral region of C2")
        self.btn = anat.Anatomy.osso_generico(tab4, 40, 80, 20, 20, "right lateral mass of C1")
        self.btn = anat.Anatomy.osso_generico(tab4, 228, 81, 20, 20, "left lateral mass of C1")
        self.btn = anat.Anatomy.osso_generico(tab4, 388, 69, 20, 20, "anterior arc of C1")
        self.btn = anat.Anatomy.osso_generico(tab4, 500, 153, 20, 20, "posterior arch of C1")
        self.btn = anat.Anatomy.vertebra(tab4, 391, 174, 20, 20, "C2")

        # C2
        self.btn = anat.Anatomy.vertebra(tab1, 204, 128, 20, 20, "C2")
        self.btn = anat.Anatomy.vertebra(tab2, 160, 164, 20, 20, "C2")

        # C3
        self.btn = anat.Anatomy.vertebra(tab1, 207, 156, 20, 20, "C3")
        self.btn = anat.Anatomy.vertebra(tab2, 163, 201, 20, 20, "C3")

        # C4
        self.btn = anat.Anatomy.vertebra(tab1, 212, 185, 20, 20, "C4")
        self.btn = anat.Anatomy.vertebra(tab2, 170, 232, 20, 20, "C4")

        # C5
        self.btn = anat.Anatomy.vertebra(tab1, 211, 214, 20, 20, "C5")
        self.btn = anat.Anatomy.vertebra(tab2, 172, 265, 20, 20, "C5")

        # C6
        self.btn = anat.Anatomy.vertebra(tab1, 216, 243, 20, 20, "C6")
        self.btn = anat.Anatomy.vertebra(tab2, 177, 298, 20, 20, "C6")

        # C7
        self.btn = anat.Anatomy.vertebra(tab1, 214, 279, 20, 20, "C7")
        self.btn = anat.Anatomy.vertebra(tab2, 192, 331, 20, 20, "C7")

        # T1
        self.btn = anat.Anatomy.vertebra(tab1, 211, 320, 20, 20, "T1")

        # T2
        self.btn = anat.Anatomy.vertebra(tab1, 213, 354, 20, 20, "T2")

        # T3
        self.btn = anat.Anatomy.vertebra(tab1, 210, 389, 20, 20, "T3")

        # T4
        self.btn = anat.Anatomy.vertebra(tab1, 215, 430, 20, 20, "T4")

        # Clavícula
        self.btn = anat.Anatomy.osso_generico(tab1, 31, 339, 20, 20, "right collarbone")
        self.btn = anat.Anatomy.osso_generico(tab1, 362, 324, 20, 20, "left collarbone")

        # Costela direita
        self.btn = anat.Anatomy.osso_generico(tab1, 134, 309, 20, 20, "1st right rib")
        self.btn = anat.Anatomy.osso_generico(tab1, 128, 339, 20, 20, "2nd right rib")
        self.btn = anat.Anatomy.osso_generico(tab1, 128, 377, 20, 20, "3rd right rib")
        self.btn = anat.Anatomy.osso_generico(tab1, 133, 414, 20, 20, "4th right rib")

        # Costela esquerda
        self.btn = anat.Anatomy.osso_generico(tab1, 294, 304, 20, 20, "1st left rib")
        self.btn = anat.Anatomy.osso_generico(tab1, 295, 335, 20, 20, "2nd left rib")
        self.btn = anat.Anatomy.osso_generico(tab1, 298, 373, 20, 20, "3rd left rib")
        self.btn = anat.Anatomy.osso_generico(tab1, 296, 419, 20, 20, "4th left rib")



        # Imagem tap 1 PA cervical
        torax_img_pa1 = wx.Image("xrd4_cerv_.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab1, bitmap=torax_img_pa1, pos=wx.DefaultPosition)

        # Imagem tap 1 Perfil cervical
        torax_img_pa1 = wx.Image("xrd5.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab2, bitmap=torax_img_pa1, pos=wx.DefaultPosition)

        # Imagem tap 3 Atlas
        torax_img_pa1 = wx.Image("xrd6.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab3, bitmap=torax_img_pa1)

        # Imagem tap 3 Atlas
        torax_img_pa1 = wx.Image("xrd1.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab4, bitmap=torax_img_pa1)


class MyPanel_img_coluna_toracica(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_img_coluna_toracica, self).__init__(parent)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA 1")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Perfil 1")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # C6
        self.btn = anat.Anatomy.vertebra(tab1, 116, 3, 20, 20, "C6")

        # C7
        self.btn = anat.Anatomy.vertebra(tab1, 117, 23, 20, 20, "C7")
        self.btn = anat.Anatomy.vertebra(tab2, 145, 15, 20, 20, "C7")


        # T1
        self.btn = anat.Anatomy.vertebra(tab1, 119, 44, 20, 20, "T1")
        self.btn = anat.Anatomy.vertebra(tab2, 150, 40, 20, 20, "T1")

        # T2
        self.btn = anat.Anatomy.vertebra(tab1, 120, 70, 20, 20, "T2")
        self.btn = anat.Anatomy.vertebra(tab2, 158, 66, 20, 20, "T2")

        # T3
        self.btn = anat.Anatomy.vertebra(tab1, 120, 105, 20, 20, "T3")
        self.btn = anat.Anatomy.vertebra(tab2, 168, 99, 20, 20, "T3")

        # T4
        self.btn = anat.Anatomy.vertebra(tab1, 120, 134, 20, 20, "T4")
        self.btn = anat.Anatomy.vertebra(tab2, 172, 123, 20, 20, "T4")

        # T5
        self.btn = anat.Anatomy.vertebra(tab1, 120, 167, 20, 20, "T5")
        self.btn = anat.Anatomy.vertebra(tab2, 173, 160, 20, 20, "T5")

        # T6
        self.btn = anat.Anatomy.vertebra(tab1, 119, 189, 20, 20, "T6")
        self.btn = anat.Anatomy.vertebra(tab2, 177, 189, 20, 20, "T6")

        # T7
        self.btn = anat.Anatomy.vertebra(tab1, 119, 219, 20, 20, "T7")
        self.btn = anat.Anatomy.vertebra(tab2, 172, 225, 20, 20, "T7")

        # T8
        self.btn = anat.Anatomy.vertebra(tab1, 119, 253, 20, 20, "T8")
        self.btn = anat.Anatomy.vertebra(tab2, 167, 263, 20, 20, "T8")

        # T9
        self.btn = anat.Anatomy.vertebra(tab1, 118, 288, 20, 20, "T9")
        self.btn = anat.Anatomy.vertebra(tab2, 156, 299, 20, 20, "T9")

        # T10
        self.btn = anat.Anatomy.vertebra(tab1, 118, 320, 20, 20, "T10")
        self.btn = anat.Anatomy.vertebra(tab2, 149, 336, 20, 20, "T10")

        # T11
        self.btn = anat.Anatomy.vertebra(tab1, 117, 355, 20, 20, "T11")
        self.btn = anat.Anatomy.vertebra(tab2, 139, 377, 20, 20, "T11")

        # T12
        self.btn = anat.Anatomy.vertebra(tab1, 119, 394, 20, 20, "T12")
        self.btn = anat.Anatomy.vertebra(tab2, 125, 423, 20, 20, "T12")

        # L1
        self.btn = anat.Anatomy.vertebra(tab1, 120, 438, 20, 20, "L1")
        self.btn = anat.Anatomy.vertebra(tab2, 111, 466, 20, 20, "L1")

        # L2
        self.btn = anat.Anatomy.vertebra(tab1, 121, 484, 20, 20, "L2")
        self.btn = anat.Anatomy.vertebra(tab2, 94, 514, 20, 20, "L2")

        # L3
        self.btn = anat.Anatomy.vertebra(tab1, 119, 529, 20, 20, "L3")


        # Imagem tap 1 PA Lombar
        torax_img_pa1 = wx.Image("xrd7.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab1, bitmap=torax_img_pa1, pos=wx.DefaultPosition)

        # Imagem tap 1 Perfil Lombar
        torax_img_pa1 = wx.Image("xrd8.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab2, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_coluna_toracolombar(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_img_coluna_toracolombar, self).__init__(parent)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA 1")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Perfil 1")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # T7
        self.btn = anat.Anatomy.vertebra(tab1, 171, 4, 20, 20, "T7")

        # T8
        self.btn = anat.Anatomy.vertebra(tab1, 170, 39, 20, 20, "T8")
        self.btn = anat.Anatomy.vertebra(tab2, 195, 18, 20, 20, "T8")

        # T9
        self.btn = anat.Anatomy.vertebra(tab1, 170, 78, 20, 20, "T9")
        self.btn = anat.Anatomy.vertebra(tab2, 180, 58, 20, 20, "T9")

        # T10
        self.btn = anat.Anatomy.vertebra(tab1, 170, 112, 20, 20, "T10")
        self.btn = anat.Anatomy.vertebra(tab2, 168, 97, 20, 20, "T10")

        # T11
        self.btn = anat.Anatomy.vertebra(tab1, 172, 157, 20, 20, "T11")
        self.btn = anat.Anatomy.vertebra(tab2, 149, 140, 20, 20, "T11")

        # T12
        self.btn = anat.Anatomy.vertebra(tab1, 170, 203, 20, 20, "T12")
        self.btn = anat.Anatomy.vertebra(tab2, 131, 189, 20, 20, "T12")

        # L1
        self.btn = anat.Anatomy.vertebra(tab1, 172, 255, 20, 20, "L1")
        self.btn = anat.Anatomy.vertebra(tab2, 114, 240, 20, 20, "L1")

        # L2
        self.btn = anat.Anatomy.vertebra(tab1, 173, 308, 20, 20, "L2")
        self.btn = anat.Anatomy.vertebra(tab2, 101, 292, 20, 20, "L2")

        # L3
        self.btn = anat.Anatomy.vertebra(tab1, 172, 370, 20, 20, "L3")
        self.btn = anat.Anatomy.vertebra(tab2, 91, 357, 20, 20, "L3")

        # L4
        self.btn = anat.Anatomy.vertebra(tab1, 171, 413, 20, 20, "L4")
        self.btn = anat.Anatomy.vertebra(tab2, 101, 420, 20, 20, "L4")

        # L5
        self.btn = anat.Anatomy.vertebra(tab1, 174, 459, 20, 20, "L5")
        self.btn = anat.Anatomy.vertebra(tab2, 113, 472, 20, 20, "L5")

        # S1
        self.btn = anat.Anatomy.vertebra(tab1, 170, 510, 20, 20, "S1")
        self.btn = anat.Anatomy.vertebra(tab2, 150, 515, 20, 20, "S1")

        # Sacro
        self.btn = anat.Anatomy.osso_generico(tab1, 171, 544, 20, 20, "sacrum")
        self.btn = anat.Anatomy.osso_generico(tab2, 185, 534, 20, 20, "sacrum")


        # Crista ilíaca
        self.btn = anat.Anatomy.osso_generico(tab1, 37, 458, 20, 20, "right iliac crest")
        self.btn = anat.Anatomy.osso_generico(tab1, 298, 466, 20, 20, "left iliac crest")

        # Imagem tap 1 PA Lombar
        torax_img_pa1 = wx.Image("xrd9.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab1, bitmap=torax_img_pa1, pos=wx.DefaultPosition)

        # Imagem tap 1 Perfil Lombar
        torax_img_pa1 = wx.Image("xrd10.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab2, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_coluna_lombar(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_img_coluna_lombar, self).__init__(parent)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA 1")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Perfil 1")

        tab4 = MyTabPanel(notebook)
        notebook.AddPage(tab4, "L5-S1")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # T11
        self.btn = anat.Anatomy.vertebra(tab1, 229, 30, 20, 20, "T11")

        # T12
        self.btn = anat.Anatomy.vertebra(tab1, 232, 68, 20, 20, "T12")
        self.btn = anat.Anatomy.vertebra(tab3, 160, 9, 20, 20, "T12")

        # L1
        self.btn = anat.Anatomy.vertebra(tab1, 230, 114, 20, 20, "L1")
        self.btn = anat.Anatomy.vertebra(tab3, 139, 66, 20, 20, "L1")

        # L2
        self.btn = anat.Anatomy.vertebra(tab1, 236, 163, 20, 20, "L2")
        self.btn = anat.Anatomy.vertebra(tab3, 113, 132, 20, 20, "L2")

        # L3
        self.btn = anat.Anatomy.vertebra(tab1, 228, 220, 20, 20, "L3")
        self.btn = anat.Anatomy.vertebra(tab3, 99, 205, 20, 20, "L3")

        # L4
        self.btn = anat.Anatomy.vertebra(tab1, 224, 275, 20, 20, "L4")
        self.btn = anat.Anatomy.vertebra(tab3, 94, 280, 20, 20, "L4")

        # L5
        self.btn = anat.Anatomy.vertebra(tab1, 223, 332, 20, 20, "L5")
        self.btn = anat.Anatomy.vertebra(tab3, 108, 359, 20, 20, "L5")

        # S1
        self.btn = anat.Anatomy.vertebra(tab1, 215, 382, 20, 20, "S1")
        self.btn = anat.Anatomy.vertebra(tab3, 155, 411, 20, 20, "S1")

        # Sacro
        self.btn = anat.Anatomy.osso_generico(tab1, 216, 423, 20, 20, "sacrum")
        self.btn = anat.Anatomy.osso_generico(tab3, 205, 434, 20, 20, "sacrum")

        # Crista ilíaca
        self.btn = anat.Anatomy.osso_generico(tab1, 59, 319, 20, 20, "right iliac crest")
        self.btn = anat.Anatomy.osso_generico(tab1, 364, 320, 20, 20, "left iliac crest")

        self.btn = anat.Anatomy.vertebra(tab4, 120, 24, 20, 20, "L3")
        self.btn = anat.Anatomy.vertebra(tab4, 99, 113, 20, 20, "L4")
        self.btn = anat.Anatomy.vertebra(tab4, 104, 205, 20, 20, "L5")
        self.btn = anat.Anatomy.vertebra(tab4, 148, 268, 20, 20, "S1")
        self.btn = anat.Anatomy.osso_generico(tab4, 199, 304, 20, 20, "sacrum")

        # Material extra
        self.btn = anat.Anatomy.material_extra(tab1, 141, 99, 20, 20, "right hypochondrium")
        self.btn = anat.Anatomy.material_extra(tab1, 128, 300, 20, 20, "right iliac fossa")

        # Imagem tap 1 PA Lombar
        torax_img_pa1 = wx.Image("xrd11.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab1, bitmap=torax_img_pa1, pos=wx.DefaultPosition)

        # Imagem tap 1 Perfil Lombar
        torax_img_pa1 = wx.Image("xrd12.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab3, bitmap=torax_img_pa1, pos=wx.DefaultPosition)

        # Imagem tap 1 Perfil Lombar
        torax_img_pa1 = wx.Image("xrd13.jpg").ConvertToBitmap()
        self.image = wx.StaticBitmap(tab4, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_coluna_sacrococcix(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_img_coluna_sacrococcix, self).__init__(parent)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP 1")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Perfil 2")

        tab3 = MyTabPanel(notebook)
        tab3.SetBackgroundColour("black")
        notebook.AddPage(tab3, "3D AP")

        tab4 = MyTabPanel(notebook)
        tab4.SetBackgroundColour("black")
        notebook.AddPage(tab4, "3D Perfil")


        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # Sacro
        self.btn = anat.Anatomy.osso_generico(tab1, 143, 194, 20, 20, "sacrum")
        self.btn = anat.Anatomy.osso_generico(tab2, 186, 159, 20, 20, "sacrum")
        self.btn = anat.Anatomy.osso_generico(tab3, 225, 151, 20, 20, "sacrum")
        self.btn = anat.Anatomy.osso_generico(tab4, 286, 156, 20, 20, "sacrum")

        self.btn = anat.Anatomy.osso_generico(tab1, 151, 355, 20, 20, "coccyx")
        self.btn = anat.Anatomy.osso_generico(tab2, 249, 330, 20, 20, "coccyx")
        self.btn = anat.Anatomy.osso_generico(tab3, 230, 277, 20, 20, "coccyx")
        self.btn = anat.Anatomy.osso_generico(tab4, 363, 360, 20, 20, "coccyx")

        dic_img = {"xrd14.jpg": tab1,
                   "xrd15.jpg": tab2,
                   "xrd16.jpg": tab3,
                   "xrd17.jpg": tab4
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_coluna_total(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_img_coluna_total, self).__init__(parent)

    def criar_btn(self):
        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabScroll(notebook)
        notebook.AddPage(tab1, "AP")
        tab1.SetBackgroundColour("black")
        tab1.SetScrollbars(1, 10, 100, 200)

        tab2 = MyTabScroll(notebook)
        notebook.AddPage(tab2, "Lateral")
        tab2.SetBackgroundColour("black")
        tab2.SetScrollbars(1, 10, 100, 200)

        tab3 = MyTabScroll(notebook)
        notebook.AddPage(tab3, "PA")
        tab3.SetBackgroundColour("black")
        tab3.SetScrollbars(1, 10, 100, 210)

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.vertebra(tab1, 209, 95, 20, 20, "C1")
        self.btn = anat.Anatomy.vertebra(tab2, 215, 139, 20, 20, "C1")
        self.btn = anat.Anatomy.vertebra(tab3, 234, 115, 20, 20, "C1")

        self.btn = anat.Anatomy.vertebra(tab1, 205, 143, 20, 20, "C2")
        self.btn = anat.Anatomy.vertebra(tab2, 212, 184, 20, 20, "C2")
        self.btn = anat.Anatomy.vertebra(tab3, 236, 166, 20, 20, "C2")

        self.btn = anat.Anatomy.vertebra(tab1, 208, 200, 20, 20, "C3")
        self.btn = anat.Anatomy.vertebra(tab2, 206, 238, 20, 20, "C3")
        self.btn = anat.Anatomy.vertebra(tab3, 236, 216, 20, 20, "C3")

        self.btn = anat.Anatomy.vertebra(tab1, 205, 252, 20, 20, "C4")
        self.btn = anat.Anatomy.vertebra(tab2, 200, 292, 20, 20, "C4")
        self.btn = anat.Anatomy.vertebra(tab3, 239, 272, 20, 20, "C4")

        self.btn = anat.Anatomy.vertebra(tab1, 207, 302, 20, 20, "C5")
        self.btn = anat.Anatomy.vertebra(tab2, 204, 347, 20, 20, "C5")
        self.btn = anat.Anatomy.vertebra(tab3, 236, 318, 20, 20, "C5")

        self.btn = anat.Anatomy.vertebra(tab1, 207, 348, 20, 20, "C6")
        self.btn = anat.Anatomy.vertebra(tab2, 210, 393, 20, 20, "C6")
        self.btn = anat.Anatomy.vertebra(tab3, 238, 361, 20, 20, "C6")

        self.btn = anat.Anatomy.vertebra(tab1, 205, 400, 20, 20, "C7")
        self.btn = anat.Anatomy.vertebra(tab2, 222, 442, 20, 20, "C7")
        self.btn = anat.Anatomy.vertebra(tab3, 237, 409, 20, 20, "C7")

        self.btn = anat.Anatomy.vertebra(tab1, 205, 449, 20, 20, "T1")
        self.btn = anat.Anatomy.vertebra(tab2, 240, 497, 20, 20, "T1")
        self.btn = anat.Anatomy.vertebra(tab3, 236, 459, 20, 20, "T1")

        self.btn = anat.Anatomy.vertebra(tab1, 207, 500, 20, 20, "T2")
        self.btn = anat.Anatomy.vertebra(tab2, 251, 549, 20, 20, "T2")
        self.btn = anat.Anatomy.vertebra(tab3, 233, 511, 20, 20, "T2")

        self.btn = anat.Anatomy.vertebra(tab1, 207, 553, 20, 20, "T3")
        self.btn = anat.Anatomy.vertebra(tab2, 265, 606, 20, 20, "T3")
        self.btn = anat.Anatomy.vertebra(tab3, 232, 562, 20, 20, "T3")

        self.btn = anat.Anatomy.vertebra(tab1, 205, 608, 20, 20, "T4")
        self.btn = anat.Anatomy.vertebra(tab2, 281, 664, 20, 20, "T4")
        self.btn = anat.Anatomy.vertebra(tab3, 230, 623, 20, 20, "T4")

        self.btn = anat.Anatomy.vertebra(tab1, 208, 661, 20, 20, "T5")
        self.btn = anat.Anatomy.vertebra(tab2, 289, 718, 20, 20, "T5")
        self.btn = anat.Anatomy.vertebra(tab3, 234, 698, 20, 20, "T5")

        self.btn = anat.Anatomy.vertebra(tab1, 206, 717, 20, 20, "T6")
        self.btn = anat.Anatomy.vertebra(tab2, 287, 780, 20, 20, "T6")
        self.btn = anat.Anatomy.vertebra(tab3, 227, 774, 20, 20, "T6")

        self.btn = anat.Anatomy.vertebra(tab1, 205, 761, 20, 20, "T7")
        self.btn = anat.Anatomy.vertebra(tab2, 288, 836, 20, 20, "T7")
        self.btn = anat.Anatomy.vertebra(tab3, 230, 843, 20, 20, "T7")

        self.btn = anat.Anatomy.vertebra(tab1, 206, 817, 20, 20, "T8")
        self.btn = anat.Anatomy.vertebra(tab2, 283, 895, 20, 20, "T8")
        self.btn = anat.Anatomy.vertebra(tab3, 235, 913, 20, 20, "T8")

        self.btn = anat.Anatomy.vertebra(tab1, 204, 871, 20, 20, "T9")
        self.btn = anat.Anatomy.vertebra(tab2, 275, 958, 20, 20, "T9")
        self.btn = anat.Anatomy.vertebra(tab3, 232, 984, 20, 20, "T9")

        self.btn = anat.Anatomy.vertebra(tab1, 203, 932, 20, 20, "T10")
        self.btn = anat.Anatomy.vertebra(tab2, 265, 1017, 20, 20, "T10")
        self.btn = anat.Anatomy.vertebra(tab3, 236, 1060, 20, 20, "T10")

        self.btn = anat.Anatomy.vertebra(tab1, 202, 993, 20, 20, "T11")
        self.btn = anat.Anatomy.vertebra(tab2, 248, 1087, 20, 20, "T11")
        self.btn = anat.Anatomy.vertebra(tab3, 242, 1142, 20, 20, "T11")

        self.btn = anat.Anatomy.vertebra(tab1, 200, 1062, 20, 20, "T12")
        self.btn = anat.Anatomy.vertebra(tab2, 234, 1156, 20, 20, "T12")
        self.btn = anat.Anatomy.vertebra(tab3, 237, 1206, 20, 20, "T12")

        self.btn = anat.Anatomy.vertebra(tab1, 200, 1148, 20, 20, "L1")
        self.btn = anat.Anatomy.vertebra(tab2, 210, 1248, 20, 20, "L1")
        self.btn = anat.Anatomy.vertebra(tab3, 233, 1289, 20, 20, "L1")

        self.btn = anat.Anatomy.vertebra(tab1, 200, 1254, 20, 20, "L2")
        self.btn = anat.Anatomy.vertebra(tab2, 182, 1335, 20, 20, "L2")
        self.btn = anat.Anatomy.vertebra(tab3, 236, 1359, 20, 20, "L2")

        self.btn = anat.Anatomy.vertebra(tab1, 199, 1341, 20, 20, "L3")
        self.btn = anat.Anatomy.vertebra(tab2, 156, 1426, 20, 20, "L3")
        self.btn = anat.Anatomy.vertebra(tab3, 234, 1443, 20, 20, "L3")

        self.btn = anat.Anatomy.vertebra(tab1, 195, 1448, 20, 20, "L4")
        self.btn = anat.Anatomy.vertebra(tab2, 145, 1523, 20, 20, "L4")
        self.btn = anat.Anatomy.vertebra(tab3, 237, 1522, 20, 20, "L4")

        self.btn = anat.Anatomy.vertebra(tab1, 197, 1540, 20, 20, "L5")
        self.btn = anat.Anatomy.vertebra(tab2, 154, 1616, 20, 20, "L5")
        self.btn = anat.Anatomy.vertebra(tab3, 243, 1620, 20, 20, "L5")

        self.btn = anat.Anatomy.vertebra(tab1, 198, 1623, 20, 20, "S1")
        self.btn = anat.Anatomy.vertebra(tab2, 176, 1690, 20, 20, "S1")
        self.btn = anat.Anatomy.vertebra(tab3, 205, 1703, 20, 20, "S1")

        self.btn = anat.Anatomy.osso_generico(tab1, 200, 1658, 20, 20, "sacrum")
        self.btn = anat.Anatomy.osso_generico(tab2, 265, 1773, 20, 20, "sacrum")
        self.btn = anat.Anatomy.osso_generico(tab3, 209, 1820, 20, 20, "sacrum")

        self.btn = anat.Anatomy.osso_generico(tab1, 199, 1759, 20, 20, "coccyx")
        self.btn = anat.Anatomy.osso_generico(tab2, 369, 1932, 20, 20, "coccyx")
        self.btn = anat.Anatomy.osso_generico(tab3, 208, 2025, 20, 20, "coccyx")


        dic_img = {"xrd18.jpg": tab1,
                   "xrd19.png": tab2,
                   "xrd20.png": tab3,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_ombro(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_img_ombro, self).__init__(parent)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)

        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        tab2.SetBackgroundColour("black")
        notebook.AddPage(tab2, "AP 3D")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "AP Rotation")

        tab4 = MyTabPanel(notebook)
        notebook.AddPage(tab4, "Axilar")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # clavícula
        self.btn = anat.Anatomy.osso_generico(tab1, 314, 52, 20, 20, "distal clavicle")
        self.btn = anat.Anatomy.osso_generico(tab2, 236, 48, 20, 20, "distal clavicle")
        self.btn = anat.Anatomy.osso_generico(tab3, 241, 47, 20, 20, "distal clavicle")
        self.btn = anat.Anatomy.osso_generico(tab4, 32, 105, 20, 20, "distal clavicle")

        # Acrômio
        self.btn = anat.Anatomy.osso_generico(tab1, 147, 71, 20, 20, "acromion")
        self.btn = anat.Anatomy.osso_generico(tab2, 142, 67, 20, 20, "acromion")
        self.btn = anat.Anatomy.osso_generico(tab3, 98, 59, 20, 20, "acromion")
        self.btn = anat.Anatomy.osso_generico(tab4, 328, 321, 20, 20, "acromion")

        # articulação acromioclavicuaar
        self.btn = anat.Anatomy.espaco_articular(tab1, 182, 53, 20, 20, "acromioclavicular joint")
        self.btn = anat.Anatomy.espaco_articular(tab2, 164, 62, 20, 20, "acromioclavicular joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 135, 43, 20, 20, "acromioclavicular joint")

        # articulação glenoumeaal
        self.btn = anat.Anatomy.espaco_articular(tab1, 232, 223, 20, 20, "glenohumeral joint")
        self.btn = anat.Anatomy.espaco_articular(tab2, 199, 146, 20, 20, "glenohumeral joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 174, 156, 20, 20, "glenohumeral joint")
        self.btn = anat.Anatomy.espaco_articular(tab4, 174, 265, 20, 20, "glenohumeral joint")

        # espaço subacromial
        self.btn = anat.Anatomy.espaco_articular(tab1, 140, 117, 20, 20, "subacromial space")
        self.btn = anat.Anatomy.espaco_articular(tab2, 133, 93, 20, 20, "subacromial space")
        self.btn = anat.Anatomy.espaco_articular(tab3, 81, 96, 20, 20, "subacromial space")

        # processo coracoide
        self.btn = anat.Anatomy.osso_generico(tab1, 288, 114, 20, 20, "coracoid process")
        self.btn = anat.Anatomy.osso_generico(tab2, 227, 106, 20, 20, "coracoid process")
        self.btn = anat.Anatomy.osso_generico(tab3, 213, 108, 20, 20, "coracoid process")
        self.btn = anat.Anatomy.osso_generico(tab4, 143, 101, 20, 20, "coracoid process")

        # glenóide
        self.btn = anat.Anatomy.osso_generico(tab1, 252, 178, 20, 20, "glenoid")
        self.btn = anat.Anatomy.osso_generico(tab2, 207, 164, 20, 20, "glenoid")
        self.btn = anat.Anatomy.osso_generico(tab3, 190, 170, 20, 20, "glenoid")

        # cabeça umeral
        self.btn = anat.Anatomy.osso_generico(tab1, 163, 151, 20, 20, "humeral head")
        self.btn = anat.Anatomy.osso_generico(tab2, 151, 147, 20, 20, "humeral head")
        self.btn = anat.Anatomy.osso_generico(tab3, 91, 163, 20, 20, "humeral head")
        self.btn = anat.Anatomy.osso_generico(tab4, 219, 195, 20, 20, "humeral head")

        self.btn = anat.Anatomy.osso_generico(tab2, 109, 263, 20, 20, "proximal humerus")
        self.btn = anat.Anatomy.osso_generico(tab4, 520, 176, 20, 20, "proximal humerus")

        # tuberosidade maior do úmero
        self.btn = anat.Anatomy.osso_generico(tab1, 62, 172, 20, 20, "greater humerus tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab2, 81, 137, 20, 20, "greater humerus tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab3, 144, 182, 20, 20, "greater humerus tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab4, 265, 104, 20, 20, "greater humerus tuberosity")

        # tuberosidade menor do úmero
        self.btn = anat.Anatomy.osso_generico(tab1, 114, 201, 20, 20, "minor humerus tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab2, 104, 165, 20, 20, "minor humerus tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab3, 175, 196, 20, 20, "minor humerus tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab4, 309, 70, 20, 20, "minor humerus tuberosity")

        # escapula
        self.btn = anat.Anatomy.osso_generico(tab2, 314, 225, 20, 20, "scapula")
        self.btn = anat.Anatomy.osso_generico(tab2, 242, 165, 20, 20, "scapula")
        self.btn = anat.Anatomy.osso_generico(tab3, 236, 171, 20, 20, "scapula")

        self.btn = anat.Anatomy.osso_generico(tab1, 392, 258, 20, 20, "medial edge of the scapula")
        self.btn = anat.Anatomy.osso_generico(tab3, 307, 250, 20, 20, "medial edge of the scapula")

        self.btn = anat.Anatomy.osso_generico(tab1, 260, 321, 20, 20, "lateral edge of the scapula")
        self.btn = anat.Anatomy.osso_generico(tab3, 205, 295, 20, 20, "lateral edge of the scapula")

        self.btn = anat.Anatomy.osso_generico(tab1, 361, 445, 20, 20, "lower scapula angle")
        self.btn = anat.Anatomy.osso_generico(tab3, 291, 394, 20, 20, "lower scapula angle")

        self.btn = anat.Anatomy.osso_generico(tab1, 431, 77, 20, 20, "upper angle of the scapula")

        # umero
        self.btn = anat.Anatomy.osso_generico(tab1, 159, 196, 20, 20, "anatomical neck of the humerus")
        self.btn = anat.Anatomy.osso_generico(tab2, 134, 155, 20, 20, "humeral metaphysis")

        self.btn = anat.Anatomy.osso_generico(tab1, 111, 250, 20, 20, "surgical neck of the humerus")
        self.btn = anat.Anatomy.osso_generico(tab3, 86, 229, 20, 20, "surgical neck of the humerus")

        # diáfise proximal
        self.btn = anat.Anatomy.osso_generico(tab1, 110, 367, 20, 20, "proximal humeral shaft")
        self.btn = anat.Anatomy.osso_generico(tab3, 76, 306, 20, 20, "proximal humeral shaft")


        dic_img = {"xrd21.png": tab1,
                   "xrd22.png": tab2,
                   "xrd23.png": tab3,
                   "xrd24.png": tab4
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_mao(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_mao, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "AP 3D")
        tab2.SetBackgroundColour("black")

        # Notebook Tab
        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Espaço articular")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # Falange distal
        self.btn = anat.Anatomy.osso_generico(tab1, 25, 231, 20, 20, "distal thumb phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 73, 192, 20, 20, "distal thumb phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 141, 46, 20, 20, "2nd finger distal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 66, 38, 20, 20, "2nd finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 222, 23, 20, 20, "3rd finger distal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 110, 8, 20, 20, "3rd finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 299, 52, 20, 20, "4th finger distal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 172, 9, 20, 20, "4th finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 390, 143, 20, 20, "5th finger distal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 227, 55, 20, 20, "5th finger distal phalanx")

        # Falange média
        self.btn = anat.Anatomy.osso_generico(tab1, 145, 90, 20, 20, "2nd finger middle phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 74, 79, 20, 20, "2nd finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 219, 78, 20, 20, "3rd finger middle phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 117, 46, 20, 20, "3rd finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 287, 100, 20, 20, "4th finger middle phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 175, 49, 20, 20, "4th finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 365, 175, 20, 20, "5rd finger middle phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 227, 89, 20, 20, "5rd finger middle phalanx")

        # Falange proximal
        self.btn = anat.Anatomy.osso_generico(tab1, 63, 273, 20, 20, "proximal phalanx of thumb")
        self.btn = anat.Anatomy.osso_generico(tab2, 80, 241, 20, 20, "proximal phalanx of thumb")

        self.btn = anat.Anatomy.osso_generico(tab1, 157, 159, 20, 20, "2nd finger proximal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 88, 135, 20, 20, "2nd finger proximal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 216, 153, 20, 20, "proximal phalanx of the 3rd finger")
        self.btn = anat.Anatomy.osso_generico(tab2, 130, 118, 20, 20, "proximal phalanx of the 3rd finger")

        self.btn = anat.Anatomy.osso_generico(tab1, 270, 176, 20, 20, "proximal phalanx of the 4th finger")
        self.btn = anat.Anatomy.osso_generico(tab2, 180, 116, 20, 20, "proximal phalanx of the 4th finger")

        self.btn = anat.Anatomy.osso_generico(tab1, 330, 217, 20, 20, "proximal phalanx of the 5th finger")
        self.btn = anat.Anatomy.osso_generico(tab2, 228, 145, 20, 20, "proximal phalanx of the 5th finger")

        # Falange proximal
        self.btn = anat.Anatomy.osso_generico(tab1, 101, 316, 20, 20, "head of the 1st metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 119, 336, 20, 20, "1st metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 96, 301, 20, 20, "1st metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 152, 364, 20, 20, "base of the 1st metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 165, 228, 20, 20, "2nd metacarpal head")
        self.btn = anat.Anatomy.osso_generico(tab1, 175, 275, 20, 20, "2nd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 121, 242, 20, 20, "2nd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 191, 331, 20, 20, "2nd metacarpal base")

        self.btn = anat.Anatomy.osso_generico(tab1, 217, 226, 20, 20, "head of the 3rd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 219, 269, 20, 20, "3rd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 160, 234, 20, 20, "3rd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 221, 328, 20, 20, "base of the 3rd metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 259, 237, 20, 20, "head of the 4th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 254, 283, 20, 20, "4th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 194, 232, 20, 20, "4th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 246, 326, 20, 20, "base of the 4th metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 296, 262, 20, 20, "head of the 5th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 284, 305, 20, 20, "5th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 233, 244, 20, 20, "5th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 272, 337, 20, 20, "base of the 5th metacarpal")

        # Trapézio
        self.btn = anat.Anatomy.osso_generico(tab1, 178, 374, 20, 20, "trapeze")
        self.btn = anat.Anatomy.osso_generico(tab2, 132, 342, 20, 20, "trapeze")

        # Trapezóide
        self.btn = anat.Anatomy.osso_generico(tab1, 198, 359, 20, 20, "trapezoid")
        self.btn = anat.Anatomy.osso_generico(tab2, 154, 335, 20, 20, "trapezoid")

        # capitato
        self.btn = anat.Anatomy.osso_generico(tab1, 225, 365, 20, 20, "capitate")
        self.btn = anat.Anatomy.osso_generico(tab2, 184, 336, 20, 20, "capitate")

        # hamato
        self.btn = anat.Anatomy.osso_generico(tab1, 249, 371, 20, 20, "hamate")
        self.btn = anat.Anatomy.osso_generico(tab2, 213, 328, 20, 20, "hamate")

        # escafoide
        self.btn = anat.Anatomy.osso_generico(tab1, 205, 401, 20, 20, "scaphoid")
        self.btn = anat.Anatomy.osso_generico(tab2, 157, 374, 20, 20, "scaphoid")

        # semilunar
        self.btn = anat.Anatomy.osso_generico(tab1, 245, 402, 20, 20, "semilunar")
        self.btn = anat.Anatomy.osso_generico(tab2, 199, 374, 20, 20, "semilunar")

        # piramidal
        self.btn = anat.Anatomy.osso_generico(tab1, 265, 386, 20, 20, "pyramidal")
        self.btn = anat.Anatomy.osso_generico(tab2, 224, 357, 20, 20, "pyramidal")

        # pisiforme
        self.btn = anat.Anatomy.osso_generico(tab1, 276, 375, 20, 20, "pisiform")
        self.btn = anat.Anatomy.osso_generico(tab2, 242, 358, 20, 20, "pisiform")

        # rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 256, 448, 20, 20, "radius")
        self.btn = anat.Anatomy.osso_generico(tab2, 180, 435, 20, 20, "radius")

        # ulna
        self.btn = anat.Anatomy.osso_generico(tab1, 308, 426, 20, 20, "ulna")
        self.btn = anat.Anatomy.osso_generico(tab2, 251, 425, 20, 20, "ulna")

        # articulação radioulnar distal
        self.btn = anat.Anatomy.espaco_articular(tab1, 277, 417, 20, 20, "distal radioulnar joint")

        self.btn = anat.Anatomy.osso_generico(tab1, 295, 387, 20, 20, "styloid process of the ulna")
        self.btn = anat.Anatomy.osso_generico(tab2, 256, 383, 20, 20, "styloid process of the ulna")

        # articulação taa 3
        self.btn = anat.Anatomy.espaco_articular(tab3, 237, 419, 20, 20, "radiocarpal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 278, 415, 20, 20, "distal radioulnar joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 232, 378, 20, 20, "intercarpal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 226, 344, 20, 20, "carpometacarpal joint")

        self.btn = anat.Anatomy.espaco_articular(tab3, 90, 300, 20, 20, "1st metacarpophalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 162, 208, 20, 20, "2nd metacarpophalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 214, 208, 20, 20, "3rd metacarpophalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 262, 221, 20, 20, "4th metacarpophalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 307, 246, 20, 20, "5th metacarpophalangeal joint")

        self.btn = anat.Anatomy.espaco_articular(tab3, 41, 251, 20, 20, "1st finger interphalangeal joint")

        self.btn = anat.Anatomy.espaco_articular(tab3, 150, 120, 20, 20, "2nd finger proximal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 216, 106, 20, 20, "3rd finger proximal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 280, 128, 20, 20, "4th finger proximal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 354, 190, 20, 20, "joint of the 5th finger proximal interphalangeal")

        self.btn = anat.Anatomy.espaco_articular(tab3, 142, 66, 20, 20, "2nd distal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 219, 43, 20, 20, "3rd finger distal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 294, 70, 20, 20, "4th finger distal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 380, 157, 20, 20, "5th finger distal interphalangeal joint")

        self.btn = anat.Anatomy.espaco_articular(tab3, 469, 92, 20, 20, "articulation of the distal interphalangeal")
        self.btn = anat.Anatomy.espaco_articular(tab3, 463, 191, 20, 20, "articulation of proximal interphalangeal joints")
        self.btn = anat.Anatomy.espaco_articular(tab3, 468, 264, 20, 20, "metacarpophalangeal joint")

        dic_img = {"xrd25.png": tab1,
                   "xrd26.png": tab2,
                   "xrd27.png": tab3
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)

class MyPanel_img_mao_idade_ossea_masc(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_mao_idade_ossea_masc, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)

        tab2 = MyTabScroll(notebook)
        notebook.AddPage(tab2, "Table")
        tab2.SetBackgroundColour("white")
        tab2.SetScrollbars(1, 10, 100, 230)

        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        # Falange distal
        self.btn = anat.Anatomy.osso_generico(tab1, 25, 231, 20, 20, "distal thumb phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 141, 46, 20, 20, "2nd finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 222, 23, 20, 20, "3rd finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 299, 52, 20, 20, "4th finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 390, 143, 20, 20, "5th finger distal phalanx")

        # Falange média
        self.btn = anat.Anatomy.osso_generico(tab1, 145, 90, 20, 20, "2nd finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 219, 78, 20, 20, "3rd finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 287, 100, 20, 20, "4th finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 365, 175, 20, 20, "5rd finger middle phalanx")

        # Falange proximal
        self.btn = anat.Anatomy.osso_generico(tab1, 63, 273, 20, 20, "proximal phalanx of thumb")

        self.btn = anat.Anatomy.osso_generico(tab1, 157, 159, 20, 20, "2nd finger proximal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 216, 153, 20, 20, "proximal phalanx of the 3rd finger")

        self.btn = anat.Anatomy.osso_generico(tab1, 270, 176, 20, 20, "proximal phalanx of the 4th finger")

        self.btn = anat.Anatomy.osso_generico(tab1, 330, 217, 20, 20, "proximal phalanx of the 5th finger")

        # Falange proximal
        self.btn = anat.Anatomy.osso_generico(tab1, 101, 316, 20, 20, "head of the 1st metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 119, 336, 20, 20, "1st metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 152, 364, 20, 20, "base of the 1st metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 165, 228, 20, 20, "2nd metacarpal head")
        self.btn = anat.Anatomy.osso_generico(tab1, 175, 275, 20, 20, "2nd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 191, 331, 20, 20, "2nd metacarpal base")

        self.btn = anat.Anatomy.osso_generico(tab1, 217, 226, 20, 20, "head of the 3rd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 219, 269, 20, 20, "3rd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 221, 328, 20, 20, "base of the 3rd metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 259, 237, 20, 20, "head of the 4th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 254, 283, 20, 20, "4th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 246, 326, 20, 20, "base of the 4th metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 296, 262, 20, 20, "head of the 5th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 284, 305, 20, 20, "5th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 272, 337, 20, 20, "base of the 5th metacarpal")

        # Trapézio
        self.btn = anat.Anatomy.osso_generico(tab1, 178, 374, 20, 20, "trapeze")

        # Trapezóide
        self.btn = anat.Anatomy.osso_generico(tab1, 198, 359, 20, 20, "trapezoid")

        # capitato
        self.btn = anat.Anatomy.osso_generico(tab1, 225, 365, 20, 20, "capitate")

        # hamato
        self.btn = anat.Anatomy.osso_generico(tab1, 249, 371, 20, 20, "hamate")

        # escafoide
        self.btn = anat.Anatomy.osso_generico(tab1, 205, 401, 20, 20, "scaphoid")

        # semilunar
        self.btn = anat.Anatomy.osso_generico(tab1, 245, 402, 20, 20, "semilunar")

        # piramidal
        self.btn = anat.Anatomy.osso_generico(tab1, 265, 386, 20, 20, "pyramidal")

        # pisiforme
        self.btn = anat.Anatomy.osso_generico(tab1, 276, 375, 20, 20, "pisiform")

        # rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 256, 448, 20, 20, "radius")

        # ulna
        self.btn = anat.Anatomy.osso_generico(tab1, 308, 426, 20, 20, "ulna")

        # articulação radioulnar distal
        self.btn = anat.Anatomy.espaco_articular(tab1, 277, 417, 20, 20, "distal radioulnar joint")

        self.btn = anat.Anatomy.osso_generico(tab1, 295, 387, 20, 20, "styloid process of the ulna")

        dic_img = {"xrd25.png": tab1,
                   "xrd2.jpg": tab2,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_mao_idade_ossea_fem(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_mao_idade_ossea_fem, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)

        tab2 = MyTabScroll(notebook)
        notebook.AddPage(tab2, "Table")
        tab2.SetBackgroundColour("white")
        tab2.SetScrollbars(1, 10, 100, 210)

        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia


        # Falange distal
        self.btn = anat.Anatomy.osso_generico(tab1, 25, 231, 20, 20, "distal thumb phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 141, 46, 20, 20, "2nd finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 222, 23, 20, 20, "3rd finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 299, 52, 20, 20, "4th finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 390, 143, 20, 20, "5th finger distal phalanx")

        # Falange média
        self.btn = anat.Anatomy.osso_generico(tab1, 145, 90, 20, 20, "2nd finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 219, 78, 20, 20, "3rd finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 287, 100, 20, 20, "4th finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 365, 175, 20, 20, "5rd finger middle phalanx")

        # Falange proximal
        self.btn = anat.Anatomy.osso_generico(tab1, 63, 273, 20, 20, "proximal phalanx of thumb")

        self.btn = anat.Anatomy.osso_generico(tab1, 157, 159, 20, 20, "2nd finger proximal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 216, 153, 20, 20, "proximal phalanx of the 3rd finger")

        self.btn = anat.Anatomy.osso_generico(tab1, 270, 176, 20, 20, "proximal phalanx of the 4th finger")

        self.btn = anat.Anatomy.osso_generico(tab1, 330, 217, 20, 20, "proximal phalanx of the 5th finger")


        # Falange proximal
        self.btn = anat.Anatomy.osso_generico(tab1, 101, 316, 20, 20, "head of the 1st metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 119, 336, 20, 20, "1st metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 152, 364, 20, 20, "base of the 1st metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 165, 228, 20, 20, "2nd metacarpal head")
        self.btn = anat.Anatomy.osso_generico(tab1, 175, 275, 20, 20, "2nd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 191, 331, 20, 20, "2nd metacarpal base")

        self.btn = anat.Anatomy.osso_generico(tab1, 217, 226, 20, 20, "head of the 3rd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 219, 269, 20, 20, "3rd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 221, 328, 20, 20, "base of the 3rd metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 259, 237, 20, 20, "head of the 4th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 254, 283, 20, 20, "4th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 246, 326, 20, 20, "base of the 4th metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 296, 262, 20, 20, "head of the 5th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 284, 305, 20, 20, "5th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab1, 272, 337, 20, 20, "base of the 5th metacarpal")


        # Trapézio
        self.btn = anat.Anatomy.osso_generico(tab1, 178, 374, 20, 20, "trapeze")

        # Trapezóide
        self.btn = anat.Anatomy.osso_generico(tab1, 198, 359, 20, 20, "trapezoid")

        # capitato
        self.btn = anat.Anatomy.osso_generico(tab1, 225, 365, 20, 20, "capitate")

        # hamato
        self.btn = anat.Anatomy.osso_generico(tab1, 249, 371, 20, 20, "hamate")

        # escafoide
        self.btn = anat.Anatomy.osso_generico(tab1, 205, 401, 20, 20, "scaphoid")

        # semilunar
        self.btn = anat.Anatomy.osso_generico(tab1, 245, 402, 20, 20, "semilunar")

        # piramidal
        self.btn = anat.Anatomy.osso_generico(tab1, 265, 386, 20, 20, "pyramidal")

        # pisiforme
        self.btn = anat.Anatomy.osso_generico(tab1, 276, 375, 20, 20, "pisiform")

        # rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 256, 448, 20, 20, "radius")

        # ulna
        self.btn = anat.Anatomy.osso_generico(tab1, 308, 426, 20, 20, "ulna")

        # articulação radioulnar distal
        self.btn = anat.Anatomy.espaco_articular(tab1, 277, 417, 20, 20, "distal radioulnar joint")

        self.btn = anat.Anatomy.osso_generico(tab1, 295, 387, 20, 20, "styloid process of the ulna")

        dic_img = {"xrd25.png": tab1,
                   "xrd3.jpg": tab2,
                   }


        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_arcos_costais(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_img_arcos_costais, self).__init__(parent)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA")

        tab2 = MyTabPanel(notebook)
        tab2.SetBackgroundColour("black")
        notebook.AddPage(tab2, "PA 3D")


        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # Solucionar problema de id antes de continuar!

        # costela direita
        self.btn1 = anat.Anatomy.osso_generico(tab1, 132, 51, 20, 20, "1st right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 132, 66, 20, 20, "1st right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 117, 68, 20, 20, "2nd right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 115, 104, 20, 20, "2nd right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 103, 95, 20, 20, "3rd right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 106, 149, 20, 20, "3rd right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 98, 123, 20, 20, "4th right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 101, 183, 20, 20, "4th right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 95, 152, 20, 20, "5th right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 91, 225, 20, 20, "5th right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 94, 188, 20, 20, "6th right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 70, 259, 20, 20, "6th right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 88, 226, 20, 20, "7th right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 65, 294, 20, 20, "7th right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 88, 264, 20, 20, "8th right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 51, 309, 20, 20, "8th right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 89, 304, 20, 20, "9th right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 112, 247, 20, 20, "9th right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 90, 350, 20, 20, "10th right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 119, 270, 20, 20, "10th right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 105, 395, 20, 20, "11th right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 125, 298, 20, 20, "11th right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 127, 405, 20, 20, "12th right rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 143, 325, 20, 20, "12th right rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 53, 74, 20, 20, "right collarbone")
        self.btn = anat.Anatomy.osso_generico(tab2, 95, 40, 20, 20, "right collarbone")

        # costela esquerda
        self.btn = anat.Anatomy.osso_generico(tab1, 249, 46, 20, 20, "1st left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 281, 67, 20, 20, "1st left rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 265, 58, 20, 20, "2nd left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 293, 107, 20, 20, "2nd left rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 277, 82, 20, 20, "3rd left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 300, 146, 20, 20, "3rd left rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 296, 113, 20, 20, "4th left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 312, 184, 20, 20, "4th left rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 306, 150, 20, 20, "5th left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 321, 225, 20, 20, "5th left rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 306, 184, 20, 20, "6th left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 337, 258, 20, 20, "6th left rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 302, 226, 20, 20, "7th left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 351, 296, 20, 20, "7th left rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 298, 264, 20, 20, "8th left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 365, 307, 20, 20, "8th left rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 297, 308, 20, 20, "9th left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 291, 238, 20, 20, "9th left rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 284, 343, 20, 20, "10th left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 297, 266, 20, 20, "10th left rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 267, 389, 20, 20, "11th left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 285, 293, 20, 20, "11th left rib")
        self.btn = anat.Anatomy.osso_generico(tab1, 246, 405, 20, 20, "12th left rib")
        self.btn = anat.Anatomy.osso_generico(tab2, 277, 322, 20, 20, "12th left rib")

        self.btn = anat.Anatomy.osso_generico(tab1, 342, 72, 20, 20, "left collarbone")
        self.btn = anat.Anatomy.osso_generico(tab2, 318, 44, 20, 20, "left collarbone")

        self.btn = anat.Anatomy.osso_generico(tab1, 24, 132, 20, 20, "right scapula body")
        self.btn = anat.Anatomy.osso_generico(tab1, 368, 135, 20, 20, "left scapula body")

        dic_img = {"xrd28.png": tab1,
                   "xrd29.png": tab2,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_clavicula(wx.Panel):
    """Panel"""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_img_clavicula, self).__init__(parent)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA")

        tab2 = MyTabPanel(notebook)
        tab2.SetBackgroundColour("black")
        notebook.AddPage(tab2, "PA 3D")


        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # clavícula
        self.btn = anat.Anatomy.osso_generico(tab1, 217, 13, 20, 20, "clavicle")

        # terço proximal da clavícula
        self.btn = anat.Anatomy.osso_generico(tab1, 133, 112, 20, 20, "proximal third of the clavicle")
        self.btn = anat.Anatomy.osso_generico(tab2, 134, 165, 20, 20, "proximal third of the clavicle")

        # terço médio da clavícula
        self.btn = anat.Anatomy.osso_generico(tab1, 220, 68, 20, 20, "middle third of the clavicle")
        self.btn = anat.Anatomy.osso_generico(tab2, 296, 127, 20, 20, "middle third of the clavicle")

        # terço médio da clavícula
        self.btn = anat.Anatomy.osso_generico(tab1, 326, 42, 20, 20, "distal third of the clavicle")
        self.btn = anat.Anatomy.osso_generico(tab2, 463, 92, 20, 20, "distal third of the clavicle")



        self.btn = anat.Anatomy.osso_generico(tab1, 416, 57, 20, 20, "acromion")
        self.btn = anat.Anatomy.osso_generico(tab2, 545, 103, 20, 20, "acromion")

        # articulação acrômio clavicuaar
        self.btn = anat.Anatomy.espaco_articular(tab1, 382, 39, 20, 20, "acromion clavicular joint")
        self.btn = anat.Anatomy.espaco_articular(tab2, 521, 96, 20, 20, "acromion clavicular joint")

        # articulação esternoclavicuaar
        self.btn = anat.Anatomy.espaco_articular(tab1, 60, 132, 20, 20, "sternoclavicular joint")
        self.btn = anat.Anatomy.espaco_articular(tab2, 62, 183, 20, 20, "sternoclavicular joint")

        # cabeça umeral
        self.btn = anat.Anatomy.osso_generico(tab1, 413, 110, 20, 20, "humeral head")
        self.btn = anat.Anatomy.osso_generico(tab2, 517, 173, 20, 20, "humeral head")

        # colo anatômico do úmero
        self.btn = anat.Anatomy.osso_generico(tab1, 422, 133, 20, 20, "anatomical neck of the humerus")
        self.btn = anat.Anatomy.osso_generico(tab2, 545, 192, 20, 20, "anatomical neck of the humerus")


        # tuberosidade maior do úmero
        self.btn = anat.Anatomy.osso_generico(tab1, 492, 111, 20, 20, "greater humerus tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab2, 611, 181, 20, 20, "greater humerus tuberosity")

        # tuberosidade menor do úmero
        self.btn = anat.Anatomy.osso_generico(tab1, 460, 152, 20, 20, "minor humerus tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab2, 569, 224, 20, 20, "minor humerus tuberosity")

        # processo coracoide
        self.btn = anat.Anatomy.osso_generico(tab1, 318, 110, 20, 20, "coracoid process")
        self.btn = anat.Anatomy.osso_generico(tab2, 443, 146, 20, 20, "coracoid process")

        dic_img = {"xrd30.png": tab1,
                   "xrd31.png": tab2,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_escapula(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_img_escapula, self).__init__(parent)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA")

        tab2 = MyTabPanel(notebook)
        tab2.SetBackgroundColour("black")
        notebook.AddPage(tab2, "PA 3D")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Draw")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # corpo da escápula
        self.btn = anat.Anatomy.osso_generico(tab1, 249, 292, 20, 20, "scapula body")
        self.btn = anat.Anatomy.osso_generico(tab2, 196, 225, 20, 20, "scapula body")
        self.btn = anat.Anatomy.osso_generico(tab3, 159, 242, 20, 20, "scapula body")
        self.btn = anat.Anatomy.osso_generico(tab3, 456, 224, 20, 20, "scapula body")

        # espinha da escápula
        self.btn = anat.Anatomy.osso_generico(tab3, 140, 192, 20, 20, "scapula spine")

        # margens da escápula
        self.btn = anat.Anatomy.osso_generico(tab1, 185, 279, 20, 20, "medial margin of the scapula")
        self.btn = anat.Anatomy.osso_generico(tab2, 144, 237, 20, 20, "medial margin of the scapula")
        self.btn = anat.Anatomy.osso_generico(tab3, 222, 288, 20, 20, "medial edge of the scapula")


        self.btn = anat.Anatomy.osso_generico(tab1, 261, 138, 20, 20, "upper margin of the scapula")
        self.btn = anat.Anatomy.osso_generico(tab2, 195, 104, 20, 20, "upper margin of the scapula")

        self.btn = anat.Anatomy.osso_generico(tab1, 292, 349, 20, 20, "lateral margin of the scapula")
        self.btn = anat.Anatomy.osso_generico(tab2, 236, 279, 20, 20, "lateral margin of the scapula")
        self.btn = anat.Anatomy.osso_generico(tab3, 109, 279, 20, 20, "lateral edge of the scapula")

        # ângulo da escápula
        self.btn = anat.Anatomy.osso_generico(tab1, 200, 99, 20, 20, "upper angle of the scapula")
        self.btn = anat.Anatomy.osso_generico(tab2, 160, 106, 20, 20, "upper angle of the scapula")
        self.btn = anat.Anatomy.osso_generico(tab3, 187, 118, 20, 20, "upper angle of the scapula")


        self.btn = anat.Anatomy.osso_generico(tab1, 219, 413, 20, 20, "lower scapula angle")
        self.btn = anat.Anatomy.osso_generico(tab2, 184, 393, 20, 20, "lower scapula angle")
        self.btn = anat.Anatomy.osso_generico(tab3, 173, 373, 20, 20, "lower scapula angle")

        # processo coracoide
        self.btn = anat.Anatomy.osso_generico(tab1, 337, 151, 20, 20, "coracoid process")
        self.btn = anat.Anatomy.osso_generico(tab2, 227, 57, 20, 20, "coracoid process")
        self.btn = anat.Anatomy.osso_generico(tab3, 266, 142, 20, 20, "coracoid process")

        # terço proximal da clavícula
        self.btn = anat.Anatomy.osso_generico(tab1, 126, 160, 20, 20, "proximal third of the clavicle")

        # terço médio da clavícula
        self.btn = anat.Anatomy.osso_generico(tab1, 250, 112, 20, 20, "middle third of the clavicle")

        # terço distal da clavícula
        self.btn = anat.Anatomy.osso_generico(tab1, 353, 85, 20, 20, "distal third of the clavicle")

        # acrômio
        self.btn = anat.Anatomy.osso_generico(tab1, 416, 101, 20, 20, "acromion")
        self.btn = anat.Anatomy.osso_generico(tab2, 325, 31, 20, 20, "acromion")
        self.btn = anat.Anatomy.osso_generico(tab3, 333, 133, 20, 20, "acromion")
        self.btn = anat.Anatomy.osso_generico(tab3, 588, 120, 20, 20, "acromion")

        # articulação acrômio clavicuaar
        self.btn = anat.Anatomy.espaco_articular(tab1, 388, 89, 20, 20, "acromion clavicular joint")

        # articulação esternoclavicuaar
        self.btn = anat.Anatomy.espaco_articular(tab1, 86, 170, 20, 20, "sternoclavicular joint")

        # umeral
        self.btn = anat.Anatomy.osso_generico(tab1, 411, 147, 20, 20, "humeral head")
        self.btn = anat.Anatomy.espaco_articular(tab1, 380, 186, 20, 20, "glenohumeral joint")

        # glenóide
        self.btn = anat.Anatomy.osso_generico(tab1, 352, 200, 20, 20, "glenoid")
        self.btn = anat.Anatomy.osso_generico(tab2, 250, 138, 20, 20, "glenoid")

        self.btn = anat.Anatomy.osso_generico(tab2, 278, 134, 20, 20, "glenoid cavity")
        self.btn = anat.Anatomy.osso_generico(tab3, 297, 189, 20, 20, "glenoid cavity")

        # colo anatômico do úmero
        self.btn = anat.Anatomy.osso_generico(tab1, 437, 169, 20, 20, "anatomical neck of the humerus")

        # tuberosidade maior do úmero
        self.btn = anat.Anatomy.osso_generico(tab1, 490, 155, 20, 20, "greater humerus tuberosity")

        # tuberosidade menor do úmero
        self.btn = anat.Anatomy.osso_generico(tab1, 464, 188, 20, 20, "minor humerus tuberosity")

        dic_img = {"xrd32.png": tab1,
                   "xrd33.png": tab2,
                   "xrd34.png": tab3,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_punho(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_punho, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "AP 3D")
        tab2.SetBackgroundColour("black")

        # Notebook Tab
        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Joint space")


        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # metacarpo
        self.btn = anat.Anatomy.osso_generico(tab1, 49, 129, 20, 20, "1st metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 54, 117, 20, 20, "1st metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 130, 70, 20, 20, "2nd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 111, 64, 20, 20, "2nd metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 185, 62, 20, 20, "3rd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 159, 56, 20, 20, "3rd metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 230, 69, 20, 20, "4th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 204, 57, 20, 20, "4th metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 268, 95, 20, 20, "5th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 245, 64, 20, 20, "5th metacarpal")

        # Trapézio
        self.btn = anat.Anatomy.osso_generico(tab1, 116, 193, 20, 20, "trapeze")
        self.btn = anat.Anatomy.osso_generico(tab2, 111, 178, 20, 20, "trapeze")

        # Trapezóide
        self.btn = anat.Anatomy.osso_generico(tab1, 149, 180, 20, 20, "trapezoid")
        self.btn = anat.Anatomy.osso_generico(tab2, 148, 167, 20, 20, "trapezoid")

        # capitato
        self.btn = anat.Anatomy.osso_generico(tab1, 184, 181, 20, 20, "capitate")
        self.btn = anat.Anatomy.osso_generico(tab2, 182, 167, 20, 20, "capitate")

        # hamato
        self.btn = anat.Anatomy.osso_generico(tab1, 224, 178, 20, 20, "hamate")
        self.btn = anat.Anatomy.osso_generico(tab2, 222, 151, 20, 20, "hamate")

        # escafoide
        self.btn = anat.Anatomy.osso_generico(tab1, 155, 227, 20, 20, "scaphoid")
        self.btn = anat.Anatomy.osso_generico(tab2, 147, 217, 20, 20, "scaphoid")

        # semilunar
        self.btn = anat.Anatomy.osso_generico(tab1, 212, 240, 20, 20, "semilunar")
        self.btn = anat.Anatomy.osso_generico(tab2, 204, 219, 20, 20, "semilunar")

        # piramidal
        self.btn = anat.Anatomy.osso_generico(tab1, 238, 221, 20, 20, "pyramidal")
        self.btn = anat.Anatomy.osso_generico(tab2, 231, 201, 20, 20, "pyramidal")

        # pisiforme
        self.btn = anat.Anatomy.osso_generico(tab1, 253, 232, 20, 20, "pisiform")
        self.btn = anat.Anatomy.osso_generico(tab2, 250, 185, 20, 20, "pisiform")

        # rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 175, 294, 20, 20, "distal radius")
        self.btn = anat.Anatomy.osso_generico(tab2, 175, 308, 20, 20, "distal radius")

        # processo estiloide do rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 138, 262, 20, 20, "radio styloid process")
        self.btn = anat.Anatomy.osso_generico(tab2, 121, 262, 20, 20, "radio styloid process")

        # ulna
        self.btn = anat.Anatomy.osso_generico(tab1, 258, 295, 20, 20, "distal ulna")
        self.btn = anat.Anatomy.osso_generico(tab2, 272, 277, 20, 20, "distal ulna")

        self.btn = anat.Anatomy.osso_generico(tab1, 278, 260, 20, 20, "styloid process of the ulna")
        self.btn = anat.Anatomy.osso_generico(tab2, 276, 222, 20, 20, "styloid process of the ulna")

        # articulação taa 3
        self.btn = anat.Anatomy.espaco_articular(tab3, 179, 250, 20, 20, "radiocarpal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 226, 297, 20, 20, "distal radioulnar joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 191, 208, 20, 20, "intercarpal joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 186, 156, 20, 20, "carpometacarpal joint")

        self.btn = anat.Anatomy.espaco_articular(tab3, 97, 184, 20, 20, "1st carpometacarpal joint")


        dic_img = {"xrd35.png": tab1,
                   "xrd36.png": tab2,
                   "xrd37.png": tab3
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_antebraco(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_antebraco, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "AP 3D")
        tab2.SetBackgroundColour("black")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # metacarpo
        self.btn = anat.Anatomy.osso_generico(tab1, 154, 30, 20, 20, "1st metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 54, 117, 20, 20, "1st metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 131, 12, 20, 20, "2nd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 111, 64, 20, 20, "2nd metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 109, 11, 20, 20, "3rd metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 159, 56, 20, 20, "3rd metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 88, 9, 20, 20, "4th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 204, 57, 20, 20, "4th metacarpal")

        self.btn = anat.Anatomy.osso_generico(tab1, 68, 13, 20, 20, "5th metacarpal")
        self.btn = anat.Anatomy.osso_generico(tab2, 245, 64, 20, 20, "5th metacarpal")

        # ossos do carpo
        self.btn = anat.Anatomy.osso_generico(tab1, 99, 59, 20, 20, "carpal bones")
        self.btn = anat.Anatomy.osso_generico(tab1, 333, 59, 20, 20, "carpal bones")


        # terço distal do rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 112, 125, 20, 20, "distal third of the radius")
        self.btn = anat.Anatomy.osso_generico(tab1, 323, 119, 20, 20, "distal third of the radius")

        # diáfise do rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 117, 217, 20, 20, "radio diaphysis")
        self.btn = anat.Anatomy.osso_generico(tab1, 316, 221, 20, 20, "radio diaphysis")

        # terço proximal do rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 108, 308, 20, 20, "proximal third of the radius")
        self.btn = anat.Anatomy.osso_generico(tab1, 312, 317, 20, 20, "proximal third of the radius")

        # terço distal da ulna
        self.btn = anat.Anatomy.osso_generico(tab1, 78, 122, 20, 20, "distal third of the ulna")
        self.btn = anat.Anatomy.osso_generico(tab1, 352, 123, 20, 20, "distal third of the ulna")

        # terço médio da ulna
        self.btn = anat.Anatomy.osso_generico(tab1, 77, 216, 20, 20, "ulnar diaphysis")
        self.btn = anat.Anatomy.osso_generico(tab1, 350, 226, 20, 20, "ulnar diaphysis")

        # terço proximal da ulna
        self.btn = anat.Anatomy.osso_generico(tab1, 80, 334, 20, 20, "proximal third of the ulna")
        self.btn = anat.Anatomy.osso_generico(tab1, 343, 346, 20, 20, "proximal third of the ulna")

        # rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 153, 217, 20, 20, "radius")
        self.btn = anat.Anatomy.osso_generico(tab1, 265, 188, 20, 20, "radius")

        # ulna
        self.btn = anat.Anatomy.osso_generico(tab1, 18, 216, 20, 20, "ulna")
        self.btn = anat.Anatomy.osso_generico(tab1, 381, 188, 20, 20, "ulna")

        # terço proximal do úmero
        self.btn = anat.Anatomy.osso_generico(tab1, 102, 456, 20, 20, "proximal third of the humerus")
        self.btn = anat.Anatomy.osso_generico(tab1, 247, 409, 20, 20, "proximal third of the humerus")

        # processo estiloide do rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 126, 77, 20, 20, "radio styloid process")
        self.btn = anat.Anatomy.osso_generico(tab1, 312, 71, 20, 20, "radio styloid process")

        # processo estiloide do ulna
        self.btn = anat.Anatomy.osso_generico(tab1, 75, 87, 20, 20, "styloid process of the ulna")
        self.btn = anat.Anatomy.osso_generico(tab1, 359, 89, 20, 20, "styloid process of the ulna")

        # tuberosidade do rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 95, 336, 20, 20, "radio tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab1, 319, 342, 20, 20, "radio tuberosity")

        # troclea
        self.btn = anat.Anatomy.osso_generico(tab1, 69, 406, 20, 20, "trochlea")

        # troclea
        self.btn = anat.Anatomy.osso_generico(tab1, 337, 415, 20, 20, "olecranon")

        self.btn = anat.Anatomy.espaco_articular(tab1, 88, 425, 20, 20, "olecranon cesspool")

        # epicôndilo medial
        self.btn = anat.Anatomy.osso_generico(tab1, 58, 432, 20, 20, "medial epicondyle")

        # epicôndilo lateral
        self.btn = anat.Anatomy.osso_generico(tab1, 115, 400, 20, 20, "lateral epicondyle")

        # cabeça do rádio
        self.btn = anat.Anatomy.osso_generico(tab1, 105, 377, 20, 20, "radio head")
        self.btn = anat.Anatomy.osso_generico(tab1, 312, 379, 20, 20, "radio head")

        # articulação radioulnar distal
        self.btn = anat.Anatomy.espaco_articular(tab1, 91, 96, 20, 20, "distal radioulnar joint")


        dic_img = {"xrd38.png": tab1,
                   "xrd42.png": tab2,
                   }


        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_cotovelo(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_cotovelo, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "AP Draw")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Lateral")

        tab4 = MyTabPanel(notebook)
        notebook.AddPage(tab4, "Perfil Draw")



        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia

        # crista supracondilar medial
        self.btn = anat.Anatomy.osso_generico(tab2, 207, 201, 20, 20, "medial supracondylar crest")
        self.btn = anat.Anatomy.osso_generico(tab2, 186, 220, 20, 20, "medial condyle")
        self.btn = anat.Anatomy.osso_generico(tab2, 137, 218, 20, 20, "lateral condyle")
        self.btn = anat.Anatomy.osso_generico(tab2, 113, 220, 20, 20, "lateral supracondylar crest")
        self.btn = anat.Anatomy.osso_generico(tab2, 126, 260, 20, 20, "radial sump")
        self.btn = anat.Anatomy.osso_generico(tab2, 175, 265, 20, 20, "coronoid fossa")

        self.btn = anat.Anatomy.osso_generico(tab1, 149, 235, 20, 20, "lateral epicondyle")
        self.btn = anat.Anatomy.osso_generico(tab2, 92, 266, 20, 20, "lateral epicondyle")
        self.btn = anat.Anatomy.osso_generico(tab2, 492, 266, 20, 20, "lateral epicondyle")
        self.btn = anat.Anatomy.osso_generico(tab3, 89, 267, 20, 20, "lateral epicondyle")
        self.btn = anat.Anatomy.osso_generico(tab4, 46, 158, 20, 20, "lateral epicondyle")

        self.btn = anat.Anatomy.osso_generico(tab1, 339, 202, 20, 20, "medial epicondyle")
        self.btn = anat.Anatomy.osso_generico(tab2, 240, 268, 20, 20, "medial epicondyle")
        self.btn = anat.Anatomy.osso_generico(tab2, 342, 275, 20, 20, "medial epicondyle")

        self.btn = anat.Anatomy.osso_generico(tab1, 201, 262, 20, 20, "humerus chapter")
        self.btn = anat.Anatomy.osso_generico(tab2, 118, 287, 20, 20, "humerus chapter")
        self.btn = anat.Anatomy.osso_generico(tab3, 141, 274, 20, 20, "humerus chapter")
        self.btn = anat.Anatomy.osso_generico(tab4, 80, 148, 20, 20, "humerus chapter")

        self.btn = anat.Anatomy.osso_generico(tab1, 280, 254, 20, 20, "trochlea")
        self.btn = anat.Anatomy.osso_generico(tab2, 190, 307, 20, 20, "trochlea")

        self.btn = anat.Anatomy.osso_generico(tab1, 278, 286, 20, 20, "coronoid process of the ulna")
        self.btn = anat.Anatomy.osso_generico(tab2, 178, 332, 20, 20, "coronoid process of the ulna")
        self.btn = anat.Anatomy.osso_generico(tab3, 149, 289, 20, 20, "coronoid process of the ulna")
        self.btn = anat.Anatomy.osso_generico(tab4, 95, 164, 20, 20, "coronoid process of the ulna")

        self.btn = anat.Anatomy.osso_generico(tab2, 146, 346, 20, 20, "radial notch of the ulna")
        self.btn = anat.Anatomy.osso_generico(tab3, 164, 358, 20, 20, "radial notch of the ulna")
        self.btn = anat.Anatomy.osso_generico(tab4, 110, 206, 20, 20, "radial notch of the ulna")

        self.btn = anat.Anatomy.osso_generico(tab3, 121, 343, 20, 20, "trochlear notch of the ulna")
        self.btn = anat.Anatomy.osso_generico(tab4, 51, 195, 20, 20, "trochlear notch of the ulna")

        self.btn = anat.Anatomy.osso_generico(tab1, 199, 318, 20, 20, "radio head")
        self.btn = anat.Anatomy.osso_generico(tab2, 117, 347, 20, 20, "radio head")
        self.btn = anat.Anatomy.osso_generico(tab2, 482, 328, 20, 20, "radio head")
        self.btn = anat.Anatomy.osso_generico(tab3, 176, 286, 20, 20, "radio head")
        self.btn = anat.Anatomy.osso_generico(tab4, 113, 152, 20, 20, "radio head")

        self.btn = anat.Anatomy.osso_generico(tab1, 209, 353, 20, 20, "radio lap")
        self.btn = anat.Anatomy.osso_generico(tab2, 110, 364, 20, 20, "radio lap")
        self.btn = anat.Anatomy.osso_generico(tab2, 477, 356, 20, 20, "radio lap")
        self.btn = anat.Anatomy.osso_generico(tab3, 216, 296, 20, 20, "radio lap")
        self.btn = anat.Anatomy.osso_generico(tab4, 145, 155, 20, 20, "radio lap")

        self.btn = anat.Anatomy.osso_generico(tab1, 196, 36, 20, 20, "distal humerus")
        self.btn = anat.Anatomy.osso_generico(tab2, 164, 149, 20, 20, "distal humerus")
        self.btn = anat.Anatomy.osso_generico(tab2, 424, 144, 20, 20, "distal humerus")
        self.btn = anat.Anatomy.osso_generico(tab3, 116, 88, 20, 20, "distal humerus")
        self.btn = anat.Anatomy.osso_generico(tab4, 31, 8, 20, 20, "distal humerus")

        self.btn = anat.Anatomy.osso_generico(tab2, 167, 394, 20, 20, "tuberosity of the ulna")

        self.btn = anat.Anatomy.osso_generico(tab1, 237, 406, 20, 20, "radio tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab2, 126, 393, 20, 20, "radio tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab2, 452, 393, 20, 20, "radio tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab3, 257, 286, 20, 20, "radio tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab4, 164, 150, 20, 20, "radio tuberosity")

        self.btn = anat.Anatomy.osso_generico(tab2, 150, 414, 20, 20, "proximal ulna")
        self.btn = anat.Anatomy.osso_generico(tab2, 422, 388, 20, 20, "proximal ulna")
        self.btn = anat.Anatomy.osso_generico(tab3, 233, 387, 20, 20, "proximal ulna")


        self.btn = anat.Anatomy.osso_generico(tab2, 101, 414, 20, 20, "proximal radio")
        self.btn = anat.Anatomy.osso_generico(tab2, 478, 417, 20, 20, "proximal radio")
        self.btn = anat.Anatomy.osso_generico(tab3, 287, 307, 20, 20, "proximal radio")

        self.btn = anat.Anatomy.espaco_articular(tab1, 258, 278, 20, 20, "umeroulnar joint")
        self.btn = anat.Anatomy.espaco_articular(tab2, 179, 319, 20, 20, "umeroulnar joint")

        self.btn = anat.Anatomy.espaco_articular(tab2, 133, 434, 20, 20, "proximal radioulnar joint")

        self.btn = anat.Anatomy.espaco_articular(tab1, 197, 300, 20, 20, "radioumeral joint")
        self.btn = anat.Anatomy.espaco_articular(tab2, 119, 329, 20, 20, "radioumeral joint")
        self.btn = anat.Anatomy.espaco_articular(tab2, 466, 319, 20, 20, "radioumeral joint")

        self.btn = anat.Anatomy.espaco_articular(tab2, 421, 239, 20, 20, "olecranon cesspool")

        self.btn = anat.Anatomy.osso_generico(tab2, 420, 275, 20, 20, "olecranon")
        self.btn = anat.Anatomy.osso_generico(tab3, 70, 391, 20, 20, "olecranon")
        self.btn = anat.Anatomy.osso_generico(tab4, 24, 225, 20, 20, "olecranon")


        self.btn = anat.Anatomy.osso_generico(tab2, 371, 290, 20, 20, "groove of the ulnar nerve")

        dic_img = {"xrd43.png": tab1,
                   "xrd44.png": tab2,
                   "xrd45.png": tab3,
                   "xrd46.png": tab4,
                   }


        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_braco(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_braco, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Lateral")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.osso_generico(tab1, 316, 88, 20, 20, "acromion")

        # úmero
        self.btn = anat.Anatomy.osso_generico(tab1, 287, 173, 20, 20, "proximal third of the humerus")
        self.btn = anat.Anatomy.osso_generico(tab2, 260, 119, 20, 20, "proximal third of the humerus")

        self.btn = anat.Anatomy.osso_generico(tab1, 230, 251, 20, 20, "middle third of the humerus")
        self.btn = anat.Anatomy.osso_generico(tab2, 176, 193, 20, 20, "middle third of the humerus")

        self.btn = anat.Anatomy.osso_generico(tab1, 169, 346, 20, 20, "distal third of the humerus")
        self.btn = anat.Anatomy.osso_generico(tab2, 106, 261, 20, 20, "distal third of the humerus")

        self.btn = anat.Anatomy.osso_generico(tab1, 335, 124, 20, 20, "humeral epiphysis")
        self.btn = anat.Anatomy.osso_generico(tab2, 281, 66, 20, 20, "humeral epiphysis")

        self.btn = anat.Anatomy.osso_generico(tab1, 293, 122, 20, 20, "great humerus tuberosity")

        self.btn = anat.Anatomy.osso_generico(tab1, 169, 346, 20, 20, "acromion")
        self.btn = anat.Anatomy.osso_generico(tab2, 273, 45, 20, 20, "acromion")


        self.btn = anat.Anatomy.osso_generico(tab1, 95, 389, 20, 20, "lateral epicondyle")
        self.btn = anat.Anatomy.osso_generico(tab1, 153, 428, 20, 20, "medial epicondyle")

        self.btn = anat.Anatomy.osso_generico(tab2, 46, 341, 20, 20, "overlapping of the lateral and medial epicondyle")

        self.btn = anat.Anatomy.osso_generico(tab1, 137, 442, 20, 20, "trochlea")

        self.btn = anat.Anatomy.osso_generico(tab1, 110, 455, 20, 20, "proximal ulna")

        self.btn = anat.Anatomy.osso_generico(tab2, 103, 383, 20, 20, "proximal ulna")


        self.btn = anat.Anatomy.osso_generico(tab1, 71, 422, 20, 20, "proximal radio")

        self.btn = anat.Anatomy.osso_generico(tab2, 25, 364, 20, 20, "olecranon")

        self.btn = anat.Anatomy.osso_generico(tab2, 141, 366, 20, 20, "proximal ulna")
        self.btn = anat.Anatomy.osso_generico(tab2, 141, 366, 20, 20, "proximal radio")
        self.btn = anat.Anatomy.osso_generico(tab1, 386, 84, 20, 20, "right collarbone")


        # fossa do olécrano
        self.btn = anat.Anatomy.espaco_articular(tab1, 359, 144, 20, 20, "glenohumeral joint")


        dic_img = {"xrd47.png": tab1,
                   "xrd48.png": tab2,
                   }


        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_bacia(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_bacia, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Lateral")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.osso_generico(tab1, 104, 17, 20, 20, "right iliac crest")
        self.btn = anat.Anatomy.osso_generico(tab1, 493, 18, 20, 20, "left iliac crest")
        self.btn = anat.Anatomy.osso_generico(tab2, 95, 86, 20, 20, "right iliac crest")
        self.btn = anat.Anatomy.osso_generico(tab2, 529, 81, 20, 20, "left iliac crest")

        self.btn = anat.Anatomy.osso_generico(tab1, 121, 65, 20, 20, "right ilium")
        self.btn = anat.Anatomy.osso_generico(tab1, 468, 63, 20, 20, "left ilium")
        self.btn = anat.Anatomy.osso_generico(tab2, 128, 137, 20, 20, "right ilium")
        self.btn = anat.Anatomy.osso_generico(tab2, 483, 139, 20, 20, "left ilium")

        self.btn = anat.Anatomy.forame(tab1, 248, 86, 20, 20, "right anterior sacral foramen")
        self.btn = anat.Anatomy.forame(tab1, 336, 93, 20, 20, "left anterior sacral foramen")
        self.btn = anat.Anatomy.forame(tab2, 275, 165, 20, 20, "right anterior sacral foramen")
        self.btn = anat.Anatomy.forame(tab2, 337, 164, 20, 20, "left anterior sacral foramen")

        self.btn = anat.Anatomy.espaco_articular(tab1, 199, 115, 20, 20, "right sacroiliac joint")
        self.btn = anat.Anatomy.espaco_articular(tab1, 391, 116, 20, 20, "left sacroiliac joint")
        self.btn = anat.Anatomy.espaco_articular(tab2, 217, 166, 20, 20, "right sacroiliac joint")
        self.btn = anat.Anatomy.espaco_articular(tab2, 399, 168, 20, 20, "left sacroiliac joint")

        self.btn = anat.Anatomy.osso_generico(tab1, 61, 155, 20, 20, "right anterior superior iliac spine")
        self.btn = anat.Anatomy.osso_generico(tab1, 523, 154, 20, 20, "left anterior superior iliac spine")
        self.btn = anat.Anatomy.osso_generico(tab2, 43, 199, 20, 20, "right anterior superior iliac spine")
        self.btn = anat.Anatomy.osso_generico(tab2, 578, 188, 20, 20, "left anterior superior iliac spine")

        self.btn = anat.Anatomy.osso_generico(tab1, 105, 216, 20, 20, "right antero-inferior iliac spine")
        self.btn = anat.Anatomy.osso_generico(tab1, 485, 218, 20, 20, "left antero-inferior iliac spine")
        self.btn = anat.Anatomy.osso_generico(tab2, 117, 261, 20, 20, "right antero-inferior iliac spine")
        self.btn = anat.Anatomy.osso_generico(tab2, 500, 257, 20, 20, "left antero-inferior iliac spine")

        self.btn = anat.Anatomy.osso_generico(tab1, 199, 258, 20, 20, "right ischial body")
        self.btn = anat.Anatomy.osso_generico(tab1, 384, 262, 20, 20, "left ischial body")
        self.btn = anat.Anatomy.osso_generico(tab2, 218, 292, 20, 20, "right ischial body")
        self.btn = anat.Anatomy.osso_generico(tab2, 389, 291, 20, 20, "left ischial body")

        self.btn = anat.Anatomy.osso_generico(tab1, 218, 304, 20, 20, "upper branch of the right pubis")
        self.btn = anat.Anatomy.osso_generico(tab1, 372, 310, 20, 20, "upper branch of the left pubis")
        self.btn = anat.Anatomy.osso_generico(tab2, 229, 333, 20, 20, "upper branch of the right pubis")
        self.btn = anat.Anatomy.osso_generico(tab2, 391, 333, 20, 20, "upper branch of the left pubis")

        self.btn = anat.Anatomy.forame(tab1, 217, 339, 20, 20, "right obturator foramen")
        self.btn = anat.Anatomy.forame(tab1, 367, 338, 20, 20, "left obturator foramen")
        self.btn = anat.Anatomy.forame(tab2, 231, 353, 20, 20, "right obturator foramen")
        self.btn = anat.Anatomy.forame(tab2, 381, 353, 20, 20, "left obturator foramen")

        self.btn = anat.Anatomy.osso_generico(tab1, 191, 348, 20, 20, "inferior branch of the right pubis")
        self.btn = anat.Anatomy.osso_generico(tab1, 393, 357, 20, 20, "inferior branch of the left pubis")
        self.btn = anat.Anatomy.osso_generico(tab2, 212, 371, 20, 20, "inferior branch of the right pubis")
        self.btn = anat.Anatomy.osso_generico(tab2, 395, 372, 20, 20, "inferior branch of the left pubis")

        self.btn = anat.Anatomy.osso_generico(tab1, 219, 383, 20, 20, "right ischial tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab1, 363, 386, 20, 20, "left ischial tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab2, 248, 383, 20, 20, "right ischial tuberosity")
        self.btn = anat.Anatomy.osso_generico(tab2, 376, 382, 20, 20, "left ischial tuberosity")

        self.btn = anat.Anatomy.espaco_articular(tab1, 294, 359, 20, 20, "pubic symphysis")
        self.btn = anat.Anatomy.espaco_articular(tab2, 311, 368, 20, 20, "pubic symphysis")

        self.btn = anat.Anatomy.osso_generico(tab1, 295, 239, 20, 20, "coccyx")
        self.btn = anat.Anatomy.osso_generico(tab2, 304, 270, 20, 20, "coccyx")

        self.btn = anat.Anatomy.osso_generico(tab1, 73, 414, 20, 20, "right femur")
        self.btn = anat.Anatomy.osso_generico(tab1, 510, 432, 20, 20, "left femur")
        self.btn = anat.Anatomy.osso_generico(tab2, 118, 437, 20, 20, "right femur")
        self.btn = anat.Anatomy.osso_generico(tab2, 500, 437, 20, 20, "left femur")

        self.btn = anat.Anatomy.osso_generico(tab1, 113, 371, 20, 20, "minor trochanter")
        self.btn = anat.Anatomy.osso_generico(tab1, 467, 380, 20, 20, "minor trochanter")
        self.btn = anat.Anatomy.osso_generico(tab2, 159, 375, 20, 20, "minor trochanter")
        self.btn = anat.Anatomy.osso_generico(tab2, 456, 373, 20, 20, "minor trochanter")

        self.btn = anat.Anatomy.osso_generico(tab1, 35, 302, 20, 20, "greater right trochanter")
        self.btn = anat.Anatomy.osso_generico(tab1, 552, 311, 20, 20, "left greater trochanter")
        self.btn = anat.Anatomy.osso_generico(tab2, 96, 303, 20, 20, "greater right trochanter")
        self.btn = anat.Anatomy.osso_generico(tab2, 510, 296, 20, 20, "left greater trochanter")

        self.btn = anat.Anatomy.osso_generico(tab1, 286, 163, 20, 20, "sacrum")
        self.btn = anat.Anatomy.osso_generico(tab2, 304, 172, 20, 20, "sacrum")

        self.btn = anat.Anatomy.osso_generico(tab1, 109, 303, 20, 20, "right femoral neck")
        self.btn = anat.Anatomy.osso_generico(tab1, 488, 311, 20, 20, "left femoral neck")
        self.btn = anat.Anatomy.osso_generico(tab2, 134, 337, 20, 20, "right femoral neck")
        self.btn = anat.Anatomy.osso_generico(tab2, 484, 337, 20, 20, "left femoral neck")

        self.btn = anat.Anatomy.osso_generico(tab1, 142, 268, 20, 20, "right femoral head")
        self.btn = anat.Anatomy.osso_generico(tab1, 462, 273, 20, 20, "left femoral head")
        self.btn = anat.Anatomy.osso_generico(tab2, 156, 316, 20, 20, "right femoral head")
        self.btn = anat.Anatomy.osso_generico(tab2, 463, 313, 20, 20, "left femoral head")

        self.btn = anat.Anatomy.osso_generico(tab1, 119, 233, 20, 20, "right acetabular ceiling")
        self.btn = anat.Anatomy.osso_generico(tab1, 470, 237, 20, 20, "left acetabular roof")

        self.btn = anat.Anatomy.osso_generico(tab1, 146, 230, 20, 20, "right acetabulum")
        self.btn = anat.Anatomy.osso_generico(tab1, 450, 230, 20, 20, "left acetabulum")
        self.btn = anat.Anatomy.osso_generico(tab2, 178, 288, 20, 20, "right acetabulum")
        self.btn = anat.Anatomy.osso_generico(tab2, 454, 286, 20, 20, "left acetabulum")

        self.btn = anat.Anatomy.vertebra(tab1, 300, 15, 20, 20, "L5")
        self.btn = anat.Anatomy.vertebra(tab2, 304, 78, 20, 20, "L5")

        self.btn = anat.Anatomy.vertebra(tab1, 297, 54, 20, 20, "S1")
        self.btn = anat.Anatomy.vertebra(tab2, 304, 145, 20, 20, "S1")

        # espaço articular
        self.btn = anat.Anatomy.espaco_articular(tab1, 164, 256, 20, 20, "right hip joint")
        self.btn = anat.Anatomy.espaco_articular(tab1, 427, 258, 20, 20, "left hip joint")

        dic_img = {"xrd49.png": tab1,
                   "xrd50.png": tab2,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_femur(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_femur, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP Proximal")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Lateal Proximal")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "AP Distal")

        tab4 = MyTabPanel(notebook)
        notebook.AddPage(tab4, "Distal Lateral")


        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.osso_generico(tab1, 164, 111, 20, 20, "foveal femoral head")

        self.btn = anat.Anatomy.osso_generico(tab1, 196, 111, 20, 20, "femoral head")
        self.btn = anat.Anatomy.osso_generico(tab2, 177, 196, 20, 20, "femoral head")

        self.btn = anat.Anatomy.osso_generico(tab1, 217, 126, 20, 20, "femoral neck")
        self.btn = anat.Anatomy.osso_generico(tab2, 202, 214, 20, 20, "femoral neck")

        self.btn = anat.Anatomy.osso_generico(tab1, 183, 79, 20, 20, "acetabulum")
        self.btn = anat.Anatomy.osso_generico(tab2, 165, 180, 20, 20, "acetabulum")

        self.btn = anat.Anatomy.osso_generico(tab1, 231, 148, 20, 20, "intertrochanteric crest")

        self.btn = anat.Anatomy.osso_generico(tab1, 271, 148, 20, 20, "greater trochanter")
        self.btn = anat.Anatomy.osso_generico(tab2, 195, 257, 20, 20, "greater trochanter")

        self.btn = anat.Anatomy.osso_generico(tab1, 212, 181, 20, 20, "minor trochanter")
        self.btn = anat.Anatomy.osso_generico(tab2, 189, 271, 20, 20, "minor trochanter")

        self.btn = anat.Anatomy.osso_generico(tab1, 229, 386, 20, 20, "femoral diaphysis")
        self.btn = anat.Anatomy.osso_generico(tab2, 323, 383, 20, 20, "femoral diaphysis")

        self.btn = anat.Anatomy.osso_generico(tab1, 234, 277, 20, 20, "proximal femoral diaphysis")
        self.btn = anat.Anatomy.osso_generico(tab2, 254, 303, 20, 20, "proximal femoral diaphysis")

        self.btn = anat.Anatomy.osso_generico(tab1, 232, 361, 20, 20, "medial femoral diaphysis")
        self.btn = anat.Anatomy.osso_generico(tab2, 303, 357, 20, 20, "medial femoral diaphysis")

        self.btn = anat.Anatomy.osso_generico(tab3, 228, 177, 20, 20, "femoral diaphysis")
        self.btn = anat.Anatomy.osso_generico(tab4, 184, 120, 20, 20, "femoral diaphysis")

        self.btn = anat.Anatomy.osso_generico(tab3, 231, 157, 20, 20, "medial femoral diaphysis")
        self.btn = anat.Anatomy.osso_generico(tab4, 193, 94, 20, 20, "medial femoral diaphysis")

        self.btn = anat.Anatomy.osso_generico(tab3, 216, 398, 20, 20, "distal femoral diaphysis")
        self.btn = anat.Anatomy.osso_generico(tab4, 194, 403, 20, 20, "distal femoral diaphysis")

        self.btn = anat.Anatomy.osso_generico(tab3, 205, 460, 20, 20, "patella")
        self.btn = anat.Anatomy.osso_generico(tab4, 242, 441, 20, 20, "patella")

        self.btn = anat.Anatomy.osso_generico(tab3, 162, 480, 20, 20, "femoral medial condyle")
        self.btn = anat.Anatomy.osso_generico(tab3, 258, 461, 20, 20, "lateral femoral condyle")

        self.btn = anat.Anatomy.osso_generico(tab4, 134, 459, 20, 20, "overlapping of the medial and lateral condyle")

        self.btn = anat.Anatomy.osso_generico(tab4, 148, 501, 20, 20, "tibial epiphysis")


        dic_img = {"xrd51.png": tab1,
                   "xrd52.png": tab2,
                   "xrd53.png": tab3,
                   "xrd54.png": tab4,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_joelho(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_joelho, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Lateral")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Horizontal Patella Vista")

        tab4 = MyTabPanel(notebook)
        notebook.AddPage(tab4, "Patella Intercondylar View")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.osso_generico(tab1, 187, 37, 20, 20, "distal femur")
        self.btn = anat.Anatomy.osso_generico(tab2, 219, 91, 20, 20, "distal femur")
        self.btn = anat.Anatomy.osso_generico(tab4, 271, 19, 20, 20, "distal femur")

        self.btn = anat.Anatomy.osso_generico(tab2, 151, 217, 20, 20, "metaphyseal region of the femur")

        self.btn = anat.Anatomy.osso_generico(tab1, 179, 10, 20, 20, "femur")
        self.btn = anat.Anatomy.osso_generico(tab2, 254, 40, 20, 20, "femur")

        self.btn = anat.Anatomy.espaco_articular(tab1, 253, 245, 20, 20, "medial knee compartment")
        self.btn = anat.Anatomy.espaco_articular(tab1, 150, 243, 20, 20, "lateral knee compartment")

        self.btn = anat.Anatomy.espaco_articular(tab1, 202, 224, 20, 20, "femorotibial joint")
        self.btn = anat.Anatomy.espaco_articular(tab4, 245, 219, 20, 20, "femorotibial joint")
        self.btn = anat.Anatomy.espaco_articular(tab4, 324, 267, 20, 20, "medial knee compartment")
        self.btn = anat.Anatomy.espaco_articular(tab4, 152, 256, 20, 20, "lateral knee compartment")


        self.btn = anat.Anatomy.osso_generico(tab1, 143, 145, 20, 20, "lateral epicondyle")

        self.btn = anat.Anatomy.osso_generico(tab1, 275, 133, 20, 20, "medial epicondyle")

        self.btn = anat.Anatomy.osso_generico(tab1, 218, 152, 20, 20, "patella")
        self.btn = anat.Anatomy.osso_generico(tab2, 73, 268, 20, 20, "patella")
        self.btn = anat.Anatomy.osso_generico(tab3, 263, 106, 20, 20, "patella")
        self.btn = anat.Anatomy.osso_generico(tab4, 271, 109, 20, 20, "patella")

        self.btn = anat.Anatomy.espaco_articular(tab2, 92, 253, 20, 20, "patellofemoral joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 256, 162, 20, 20, "patellofemoral joint")


        self.btn = anat.Anatomy.osso_generico(tab3, 258, 196, 20, 20, "patellar femoral surface")

        self.btn = anat.Anatomy.osso_generico(tab2, 151, 350, 20, 20, "tibial condyles")

        self.btn = anat.Anatomy.osso_generico(tab2, 151, 397, 20, 20, "tibial tuberosity")

        self.btn = anat.Anatomy.osso_generico(tab1, 133, 225, 20, 20, "lateral femoral condyle")
        self.btn = anat.Anatomy.osso_generico(tab2, 199, 268, 20, 20, "lateral femoral condyle")
        self.btn = anat.Anatomy.osso_generico(tab3, 153, 212, 20, 20, "lateral femoral condyle")
        self.btn = anat.Anatomy.osso_generico(tab4, 122, 239, 20, 20, "lateral femoral condyle")

        self.btn = anat.Anatomy.espaco_articular(tab3, 332, 168, 20, 20, "patellofemoral joint in the medial aspect")
        self.btn = anat.Anatomy.espaco_articular(tab3, 221, 168, 20, 20, "lateral patellofemoral joint")


        self.btn = anat.Anatomy.osso_generico(tab1, 287, 231, 20, 20, "medial femoral condyle")
        self.btn = anat.Anatomy.osso_generico(tab2, 186, 284, 20, 20, "medial femoral condyle")
        self.btn = anat.Anatomy.osso_generico(tab3, 351, 191, 20, 20, "medial femoral condyle")
        self.btn = anat.Anatomy.osso_generico(tab4, 367, 238, 20, 20, "medial femoral condyle")


        self.btn = anat.Anatomy.forame(tab1, 209, 213, 20, 20, "intercondylar fossa")
        self.btn = anat.Anatomy.forame(tab4, 243, 194, 20, 20, "intercondylar fossa")

        self.btn = anat.Anatomy.osso_generico(tab1, 128, 279, 20, 20, "lateral tibial condyle")

        self.btn = anat.Anatomy.osso_generico(tab1, 281, 276, 20, 20, "medial tibial condyle")

        self.btn = anat.Anatomy.osso_generico(tab1, 203, 238, 20, 20, "intercondylar eminence")
        self.btn = anat.Anatomy.osso_generico(tab2, 177, 301, 20, 20, "intercondylar eminence")
        self.btn = anat.Anatomy.osso_generico(tab4, 246, 260, 20, 20, "intercondylar eminence")

        self.btn = anat.Anatomy.osso_generico(tab4, 228, 254, 20, 20, "medial intercondylar tubercle")
        self.btn = anat.Anatomy.osso_generico(tab4, 266, 248, 20, 20, "lateral intercondylar tubercle")


        self.btn = anat.Anatomy.osso_generico(tab1, 113, 339, 20, 20, "fibular head")

        self.btn = anat.Anatomy.osso_generico(tab1, 132, 433, 20, 20, "proximal fibula")
        self.btn = anat.Anatomy.osso_generico(tab2, 259, 414, 20, 20, "proximal fibula")

        self.btn = anat.Anatomy.osso_generico(tab2, 287, 462, 20, 20, "fibula")

        self.btn = anat.Anatomy.osso_generico(tab1, 238, 358, 20, 20, "proximal tibia")
        self.btn = anat.Anatomy.osso_generico(tab2, 203, 428, 20, 20, "proximal tibia")
        self.btn = anat.Anatomy.osso_generico(tab4, 240, 350, 20, 20, "proximal tibia")

        self.btn = anat.Anatomy.osso_generico(tab1, 205, 328, 20, 20, "metaphyseal region of the tibia")

        self.btn = anat.Anatomy.osso_generico(tab1, 214, 464, 20, 20, "tibia")
        self.btn = anat.Anatomy.osso_generico(tab2, 202, 465, 20, 20, "tibia")

        self.btn = anat.Anatomy.osso_generico(tab2, 158, 307, 20, 20, "tibial plateau")


        self.btn = anat.Anatomy.osso_generico(tab2, 197, 211, 20, 20, "abdomen femoral tuberosity")

        self.btn = anat.Anatomy.osso_generico(tab2, 217, 272, 20, 20, "fabela")

        self.btn = anat.Anatomy.parte_mole(tab2, 100, 181, 20, 20, "suprapatellar fat pad")


        dic_img = {"xrd55.png": tab1,
                   "xrd56.png": tab2,
                   "xrd57.png": tab3,
                   "xrd58.png": tab4,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_perna(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_perna, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Lateral")


        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.osso_generico(tab1, 162, 102, 20, 20, "medial tibial condyle")
        self.btn = anat.Anatomy.osso_generico(tab1, 90, 137, 20, 20, "lateral tibial condyle")

        self.btn = anat.Anatomy.osso_generico(tab1, 60, 12, 20, 20, "distal femur")

        self.btn = anat.Anatomy.osso_generico(tab1, 88, 56, 20, 20, "patella")
        self.btn = anat.Anatomy.osso_generico(tab2, 22, 66, 20, 20, "patella")

        self.btn = anat.Anatomy.osso_generico(tab1, 85, 164, 20, 20, "fibular head")
        self.btn = anat.Anatomy.osso_generico(tab2, 119, 86, 20, 20, "fibular head")

        self.btn = anat.Anatomy.osso_generico(tab2, 81, 136, 20, 20, "tibial tuberosity")

        self.btn = anat.Anatomy.osso_generico(tab1, 236, 272, 20, 20, "tibia")
        self.btn = anat.Anatomy.osso_generico(tab2, 179, 248, 20, 20, "tibia")

        self.btn = anat.Anatomy.osso_generico(tab1, 166, 180, 20, 20, "proximal third of tibia")
        self.btn = anat.Anatomy.osso_generico(tab2, 134, 164, 20, 20, "proximal third of tibia")

        self.btn = anat.Anatomy.osso_generico(tab1, 218, 255, 20, 20, "medial third of tibia")
        self.btn = anat.Anatomy.osso_generico(tab2, 201, 262, 20, 20, "medial third of tibia")

        self.btn = anat.Anatomy.osso_generico(tab1, 317, 392, 20, 20, "distal third of tibia")
        self.btn = anat.Anatomy.osso_generico(tab2, 276, 368, 20, 20, "distal third of tibia")


        self.btn = anat.Anatomy.osso_generico(tab1, 177, 269, 20, 20, "fibula")
        self.btn = anat.Anatomy.osso_generico(tab2, 241, 245, 20, 20, "fibula")

        self.btn = anat.Anatomy.osso_generico(tab1, 138, 222, 20, 20, "proximal third of the fibula")
        self.btn = anat.Anatomy.osso_generico(tab2, 170, 153, 20, 20, "proximal third of the fibula")

        self.btn = anat.Anatomy.osso_generico(tab1, 209, 308, 20, 20, "medial third of the fibula")
        self.btn = anat.Anatomy.osso_generico(tab2, 225, 227, 20, 20, "medial third of the fibula")

        self.btn = anat.Anatomy.osso_generico(tab1, 296, 417, 20, 20, "distal third of the fibula")
        self.btn = anat.Anatomy.osso_generico(tab2, 295, 345, 20, 20, "distal third of the fibula")

        self.btn = anat.Anatomy.espaco_articular(tab1, 104, 149, 20, 20, "proximal tibiofibular joint")
        self.btn = anat.Anatomy.espaco_articular(tab1, 335, 471, 20, 20, "distal tibiofibular joint")

        self.btn = anat.Anatomy.espaco_articular(tab1, 110, 94, 20, 20, "femorotibial joint")

        self.btn = anat.Anatomy.osso_generico(tab1, 390, 441, 20, 20, "medial malleolus")
        self.btn = anat.Anatomy.osso_generico(tab2, 321, 443, 20, 20, "medial malleolus")

        self.btn = anat.Anatomy.osso_generico(tab1, 346, 498, 20, 20, "lateral malleolus")

        self.btn = anat.Anatomy.osso_generico(tab1, 136, 39, 20, 20, "femoral medial condyle")
        self.btn = anat.Anatomy.osso_generico(tab1, 52, 88, 20, 20, "lateral femoral condyle")
        self.btn = anat.Anatomy.osso_generico(tab2, 80, 48, 20, 20, "overlapping of the medial and lateral femoral condyles")


        dic_img = {"xrd59.png": tab1,
                   "xrd60.png": tab2,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_tornozelo(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_tornozelo, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Lateral")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Vista Mortise")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.osso_generico(tab1, 181, 90, 20, 20, "tibia")
        self.btn = anat.Anatomy.osso_generico(tab2, 124, 9, 20, 20, "tibia")
        self.btn = anat.Anatomy.osso_generico(tab3, 176, 76, 20, 20, "tibia")

        self.btn = anat.Anatomy.osso_generico(tab1, 197, 107, 20, 20, "distal tibia")

        self.btn = anat.Anatomy.osso_generico(tab1, 267, 33, 20, 20, "fibula diaphysis")
        self.btn = anat.Anatomy.osso_generico(tab3, 276, 25, 20, 20, "fibula diaphysis")

        self.btn = anat.Anatomy.espaco_articular(tab1, 196, 319, 20, 20, "tibiotalar joint")

        self.btn = anat.Anatomy.osso_generico(tab1, 271, 136, 20, 20, "fibula")
        self.btn = anat.Anatomy.osso_generico(tab2, 91, 126, 20, 20, "fibula")
        self.btn = anat.Anatomy.osso_generico(tab3, 272, 145, 20, 20, "fibula")

        self.btn = anat.Anatomy.osso_generico(tab1, 269, 81, 20, 20, "distal fibula")

        self.btn = anat.Anatomy.espaco_articular(tab1, 254, 270, 20, 20, "distal tibiofibular joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 237, 296, 20, 20, "distal tibiofibular joint")

        self.btn = anat.Anatomy.espaco_articular(tab3, 244, 362, 20, 20, "fibulotalar joint")

        self.btn = anat.Anatomy.espaco_articular(tab1, 195, 319, 20, 20, "tibiotalar joint")
        self.btn = anat.Anatomy.espaco_articular(tab2, 145, 192, 20, 20, "tibiotalar joint")
        self.btn = anat.Anatomy.espaco_articular(tab3, 190, 327, 20, 20, "tibiotalar joint")

        self.btn = anat.Anatomy.osso_generico(tab3, 189, 345, 20, 20, "Mortise ankle")


        self.btn = anat.Anatomy.osso_generico(tab1, 176, 373, 20, 20, "talus")
        self.btn = anat.Anatomy.osso_generico(tab2, 182, 214, 20, 20, "talus")
        self.btn = anat.Anatomy.osso_generico(tab3, 224, 365, 20, 20, "talus")

        self.btn = anat.Anatomy.osso_generico(tab2, 55, 340, 20, 20, "calcaneus")

        self.btn = anat.Anatomy.osso_generico(tab2, 261, 263, 20, 20, "navicular")

        self.btn = anat.Anatomy.osso_generico(tab2, 226, 350, 20, 20, "cuboid")

        self.btn = anat.Anatomy.osso_generico(tab2, 254, 395, 20, 20, "5th metatarsal base")

        self.btn = anat.Anatomy.osso_generico(tab1, 109, 324, 20, 20, "medial malleolus")
        self.btn = anat.Anatomy.osso_generico(tab1, 288, 355, 20, 20, "lateral malleolus")
        self.btn = anat.Anatomy.osso_generico(tab3, 107, 323, 20, 20, "medial malleolus")

        self.btn = anat.Anatomy.osso_generico(tab1, 346, 498, 20, 20, "lateral malleolus")
        self.btn = anat.Anatomy.osso_generico(tab2, 109, 221, 20, 20, "lateral malleolus")
        self.btn = anat.Anatomy.osso_generico(tab3, 288, 341, 20, 20, "lateral malleolus")

        dic_img = {"xrd61.png": tab1,
                   "xrd62.png": tab2,
                   "xrd63.png": tab3,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_pe(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_pe, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Oblique")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Lateral")

        tab4 = MyTabPanel(notebook)
        notebook.AddPage(tab4, "Lateral with load")

        tab5 = MyTabPanel(notebook)
        notebook.AddPage(tab5, "Joints")

        tab6 = MyTabPanel(notebook)
        notebook.AddPage(tab6, "Draw joints")

        tab7 = MyTabPanel(notebook)
        notebook.AddPage(tab7, "Bones accessories")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.osso_generico(tab1, 148, 85, 20, 20, "1st finger distal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 160, 68, 20, 20, "1st finger distal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab3, 478, 136, 20, 20, "phalanges")
        self.btn = anat.Anatomy.osso_generico(tab4, 511, 145, 20, 20, "phalanges")

        self.btn = anat.Anatomy.osso_generico(tab1, 193, 97, 20, 20, "2nd finger distal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 199, 54, 20, 20, "2nd finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 225, 114, 20, 20, "3rd finger distal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 231, 78, 20, 20, "3rd finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 254, 142, 20, 20, "4th finger distal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 257, 100, 20, 20, "4th finger distal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 289, 167, 20, 20, "5th finger distal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 284, 127, 20, 20, "5th finger distal phalanx")

        # Falange média
        self.btn = anat.Anatomy.osso_generico(tab1, 190, 117, 20, 20, "2nd finger middle phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 189, 79, 20, 20, "2nd finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 222, 135, 20, 20, "3rd finger middle phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 219, 96, 20, 20, "3rd finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 253, 155, 20, 20, "4th finger middle phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 250, 117, 20, 20, "4th finger middle phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 286, 176, 20, 20, "5rd finger middle phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 282, 145, 20, 20, "5rd finger middle phalanx")

        # Falange proximal
        self.btn = anat.Anatomy.osso_generico(tab1, 135, 147, 20, 20, "proximal phalanx of the 1st finger")
        self.btn = anat.Anatomy.osso_generico(tab2, 148, 131, 20, 20, "proximal phalanx of the 1st finger")

        self.btn = anat.Anatomy.osso_generico(tab1, 192, 154, 20, 20, "2nd finger proximal phalanx")
        self.btn = anat.Anatomy.osso_generico(tab2, 191, 131, 20, 20, "2nd finger proximal phalanx")

        self.btn = anat.Anatomy.osso_generico(tab1, 222, 164, 20, 20, "proximal phalanx of the 3rd finger")
        self.btn = anat.Anatomy.osso_generico(tab2, 220, 135, 20, 20, "proximal phalanx of the 3rd finger")

        self.btn = anat.Anatomy.osso_generico(tab1, 252, 183, 20, 20, "proximal phalanx of the 4th finger")
        self.btn = anat.Anatomy.osso_generico(tab2, 250, 153, 20, 20, "proximal phalanx of the 4th finger")

        self.btn = anat.Anatomy.osso_generico(tab1, 287, 208, 20, 20, "proximal phalanx of the 5th finger")
        self.btn = anat.Anatomy.osso_generico(tab2, 278, 172, 20, 20, "proximal phalanx of the 5th finger")

        #  metatarso
        self.btn = anat.Anatomy.osso_generico(tab1, 160, 267, 20, 20, "1st metatarsal")
        self.btn = anat.Anatomy.osso_generico(tab2, 151, 239, 20, 20, "1st metatarsal")
        self.btn = anat.Anatomy.osso_generico(tab3, 337, 98, 20, 20, "metatarsal bones")
        self.btn = anat.Anatomy.osso_generico(tab4, 373, 114, 20, 20, "metatarsal bones")

        self.btn = anat.Anatomy.osso_generico(tab1, 208, 271, 20, 20, "2nd metatarsal")
        self.btn = anat.Anatomy.osso_generico(tab2, 184, 242, 20, 20, "2nd metatarsal")

        self.btn = anat.Anatomy.osso_generico(tab1, 232, 271, 20, 20, "3rd metatarsal")
        self.btn = anat.Anatomy.osso_generico(tab2, 216, 243, 20, 20, "3rd metatarsal")

        self.btn = anat.Anatomy.osso_generico(tab1, 251, 272, 20, 20, "4th metatarsal")
        self.btn = anat.Anatomy.osso_generico(tab2, 246, 242, 20, 20, "4th metatarsal")

        self.btn = anat.Anatomy.osso_generico(tab1, 280, 275, 20, 20, "5th metatarsal")
        self.btn = anat.Anatomy.osso_generico(tab2, 285, 248, 20, 20, "5th metatarsal")

        self.btn = anat.Anatomy.osso_generico(tab1, 287, 357, 20, 20, "5th metatarsal base")
        self.btn = anat.Anatomy.osso_generico(tab2, 296, 356, 20, 20, "5th metatarsal base")

        # cuneiforme médio
        self.btn = anat.Anatomy.osso_generico(tab1, 172, 334, 20, 20, "medium cuneiform")
        self.btn = anat.Anatomy.osso_generico(tab2, 139, 316, 20, 20, "medium cuneiform")

        # cuneiforme intermédio
        self.btn = anat.Anatomy.osso_generico(tab1, 208, 348, 20, 20, "intermediate cuneiform")
        self.btn = anat.Anatomy.osso_generico(tab2, 171, 336, 20, 20, "intermediate cuneiform")

        # cuneiforme lateral
        self.btn = anat.Anatomy.osso_generico(tab1, 234, 365, 20, 20, "lateral cuneiform")
        self.btn = anat.Anatomy.osso_generico(tab2, 203, 350, 20, 20, "lateral cuneiform")

        # cuboide
        self.btn = anat.Anatomy.osso_generico(tab1, 259, 400, 20, 20, "cuboid")
        self.btn = anat.Anatomy.osso_generico(tab2, 252, 392, 20, 20, "cuboid")

        # navicular
        self.btn = anat.Anatomy.osso_generico(tab1, 179, 404, 20, 20, "navicular")
        self.btn = anat.Anatomy.osso_generico(tab2, 142, 379, 20, 20, "navicular")
        self.btn = anat.Anatomy.osso_generico(tab3, 235, 127, 20, 20, "navicular")

        self.btn = anat.Anatomy.osso_generico(tab1, 128, 209, 20, 20, "medial sesamoid")
        self.btn = anat.Anatomy.osso_generico(tab2, 162, 194, 20, 20, "medial sesamoid")

        self.btn = anat.Anatomy.osso_generico(tab1, 154, 216, 20, 20, "lateral sesamoid")
        self.btn = anat.Anatomy.osso_generico(tab2, 181, 192, 20, 20, "lateral sesamoid")

        self.btn = anat.Anatomy.osso_generico(tab1, 120, 236, 20, 20, "sesamoid")
        self.btn = anat.Anatomy.osso_generico(tab2, 138, 187, 20, 20, "sesamoid")
        self.btn = anat.Anatomy.osso_generico(tab3, 389, 243, 20, 20, "sesamoid")

        # tálus
        self.btn = anat.Anatomy.osso_generico(tab1, 189, 445, 20, 20, "talus")
        self.btn = anat.Anatomy.osso_generico(tab2, 141, 436, 20, 20, "talus")
        self.btn = anat.Anatomy.osso_generico(tab3, 243, 45, 20, 20, "tarsal bones")
        self.btn = anat.Anatomy.osso_generico(tab4, 272, 70, 20, 20, "tarsal bones")

        self.btn = anat.Anatomy.forame(tab3, 162, 132, 20, 20, "tarsal sinus")

        # semilunar
        self.btn = anat.Anatomy.osso_generico(tab1, 245, 402, 20, 20, "semilunar")
        self.btn = anat.Anatomy.osso_generico(tab2, 199, 374, 20, 20, "semilunar")

        # calcâneo
        self.btn = anat.Anatomy.osso_generico(tab1, 260, 451, 20, 20, "calcaneus")
        self.btn = anat.Anatomy.osso_generico(tab2, 258, 502, 20, 20, "calcaneus")
        self.btn = anat.Anatomy.osso_generico(tab3, 76, 196, 20, 20, "calcaneus")
        self.btn = anat.Anatomy.osso_generico(tab4, 73, 171, 20, 20, "calcaneus")

        self.btn = anat.Anatomy.forame(tab4, 250, 218, 20, 20, "lateral longitudinal arch of the foot")


        # tíbia
        self.btn = anat.Anatomy.osso_generico(tab1, 163, 552, 20, 20, "distal tibia")
        self.btn = anat.Anatomy.osso_generico(tab2, 80, 490, 20, 20, "distal tibia")
        self.btn = anat.Anatomy.osso_generico(tab3, 75, 57, 20, 20, "distal tibia")

        # fíbula
        self.btn = anat.Anatomy.osso_generico(tab1, 279, 556, 20, 20, "distal fibula")
        self.btn = anat.Anatomy.osso_generico(tab2, 87, 587, 20, 20, "distal fibula")
        self.btn = anat.Anatomy.osso_generico(tab3, 94, 106, 20, 20, "distal fibula")


        # articulaaão
        self.btn = anat.Anatomy.espaco_articular(tab5, 137, 186, 20, 20, "1st metatarsophalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 193, 182, 20, 20, "2nd metatarsophalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 221, 194, 20, 20, "3rd metatarsophalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 250, 207, 20, 20, "4th metatarsophalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 286, 231, 20, 20, "5th metatarsophalangeal joint")

        self.btn = anat.Anatomy.espaco_articular(tab5, 174, 313, 20, 20, "1st tarsometatarsal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 211, 336, 20, 20, "2nd tarsometatarsal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 232, 337, 20, 20, "3rd tarsometatarsal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 253, 351, 20, 20, "4th tarsometatarsal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 275, 364, 20, 20, "5th tarsometatarsal joint")

        self.btn = anat.Anatomy.espaco_articular(tab6, 194, 266, 20, 20, "Lisfranc joint")
        self.btn = anat.Anatomy.espaco_articular(tab6, 219, 350, 20, 20, "Chopart articulation")

        self.btn = anat.Anatomy.espaco_articular(tab5, 138, 118, 20, 20, "halux interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab6, 252, 51, 20, 20, "halux interphalangeal joint")

        self.btn = anat.Anatomy.espaco_articular(tab5, 188, 128, 20, 20,
                                                  "2nd finger proximal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 222, 145, 20, 20,
                                                  "3rd finger proximal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 253, 164, 20, 20,
                                                  "4th finger proximal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 288, 183, 20, 20,
                                                  "joint of the 5th finger proximal interphalangeal")

        self.btn = anat.Anatomy.espaco_articular(tab5, 192, 110, 20, 20,
                                                  "2nd distal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 224, 129, 20, 20,
                                                  "3rd finger distal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 253, 146, 20, 20,
                                                  "4th finger distal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 284, 166, 20, 20,
                                                  "5th finger distal interphalangeal joint")

        self.btn = anat.Anatomy.espaco_articular(tab6, 220, 18, 20, 20, "articulation of the distal interphalangeal")
        self.btn = anat.Anatomy.espaco_articular(tab6, 217, 52, 20, 20, "proximal interphalangeal joint")
        self.btn = anat.Anatomy.espaco_articular(tab6, 287, 118, 20, 20, "metatarsophalangeal joint")

        self.btn = anat.Anatomy.espaco_articular(tab5, 237, 419, 20, 20, "radiocarpal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 278, 415, 20, 20, "distal radioulnar joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 232, 378, 20, 20, "intercarpal joint")
        self.btn = anat.Anatomy.espaco_articular(tab5, 226, 344, 20, 20, "carpometacarpal joint")

        self.btn = anat.Anatomy.espaco_articular(tab6, 322, 120, 20, 20, "forefoot joints")
        self.btn = anat.Anatomy.espaco_articular(tab6, 327, 291, 20, 20, "midfoot joints")
        self.btn = anat.Anatomy.espaco_articular(tab6, 331, 416, 20, 20, "hindfoot joints")

        self.btn = anat.Anatomy.espaco_articular(tab6, 117, 333, 20, 20, "Lisfranc joint")
        self.btn = anat.Anatomy.espaco_articular(tab6, 140, 362, 20, 20, "Chopart articulation")

        # Ossos acessórios do pé
        self.btn = anat.Anatomy.osso_generico(tab7, 431, 118, 20, 20, "Os trigonum")
        self.btn = anat.Anatomy.osso_generico(tab7, 431, 118, 20, 20, "Os trigonum")

        self.btn = anat.Anatomy.osso_generico(tab7, 207, 276, 20, 20, "Os vesalianum")
        self.btn = anat.Anatomy.osso_generico(tab7, 464, 243, 20, 20, "Os vesalianum")

        self.btn = anat.Anatomy.osso_generico(tab7, 201, 291, 20, 20, "Os peroneum")
        self.btn = anat.Anatomy.osso_generico(tab7, 455, 223, 20, 20, "Os peroneum")

        self.btn = anat.Anatomy.osso_generico(tab7, 160, 197, 20, 20, "Os intermetatarseum")
        self.btn = anat.Anatomy.osso_generico(tab7, 210, 218, 20, 20, "Os intermetatarseum")

        self.btn = anat.Anatomy.osso_generico(tab7, 105, 291, 20, 20, "Os tibiale externum")
        self.btn = anat.Anatomy.osso_generico(tab7, 487, 204, 20, 20, "Os tibiale externum")

        self.btn = anat.Anatomy.osso_generico(tab7, 513, 170, 20, 20, "Os supranaviculare")
        self.btn = anat.Anatomy.osso_generico(tab7, 136, 281, 20, 20, "Os supranaviculare")

        self.btn = anat.Anatomy.osso_generico(tab7, 500, 156, 20, 20, "Os supratalare")

        dic_img = {"xrd64.png": tab1,
                   "xrd65.png": tab2,
                   "xrd66.png": tab3,
                   "xrd67.png": tab4,
                   "xrd68.png": tab5,
                   "xrd69.png": tab6,
                   "xrd4.jpg": tab7
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_calcaneo(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_calcaneo, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Lateral")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "AP 3D")
        tab3.SetBackgroundColour("black")

        tab4 = MyTabPanel(notebook)
        notebook.AddPage(tab4, "Perfil 3D")
        tab4.SetBackgroundColour("black")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        # calcâneo
        self.btn = anat.Anatomy.osso_generico(tab1, 140, 340, 20, 20, "calcaneus")
        self.btn = anat.Anatomy.osso_generico(tab2, 371, 300, 20, 20, "calcaneus")
        self.btn = anat.Anatomy.osso_generico(tab3, 171, 440, 20, 20, "calcaneus")
        self.btn = anat.Anatomy.osso_generico(tab4, 476, 261, 20, 20, "calcaneus")

        # navicular
        self.btn = anat.Anatomy.osso_generico(tab2, 105, 405, 20, 20, "navicular")

        self.btn = anat.Anatomy.forame(tab2, 209, 328, 20, 20, "tarsal sinus")

        # tálus
        self.btn = anat.Anatomy.osso_generico(tab2, 168, 291, 20, 20, "talus")

        # tíbia
        self.btn = anat.Anatomy.osso_generico(tab2, 172, 96, 20, 20, "distal tibia")

        dic_img = {"xrd71.png": tab1,
                   "xrd72.png": tab2,
                   "xrd73.png": tab3,
                   "xrd74.png": tab4,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_abdomen(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_abdomen, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP Anotado")
        tab1.SetBackgroundColour("black")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "AP")
        tab2.SetBackgroundColour("black")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.organ_generico(tab1, 85, 14, 20, 20, "liver")
        self.btn = anat.Anatomy.organ_generico(tab1, 375, 5, 20, 20, "spleen")
        self.btn = anat.Anatomy.osso_generico(tab1, 375, 5, 20, 20, "11th left rib")
        self.btn = anat.Anatomy.organ_generico(tab1, 138, 90, 20, 20, "right kidney")
        self.btn = anat.Anatomy.organ_generico(tab1, 308, 103, 20, 20, "left kidney")
        self.btn = anat.Anatomy.organ_generico(tab1, 153, 201, 20, 20, "right psoas muscle")
        self.btn = anat.Anatomy.organ_generico(tab1, 290, 207, 20, 20, "left psoas muscle")
        self.btn = anat.Anatomy.osso_generico(tab1, 221, 95, 20, 20, "spinous process of L1")
        self.btn = anat.Anatomy.osso_generico(tab1, 204, 166, 20, 20, "right pedicle of L3")
        self.btn = anat.Anatomy.osso_generico(tab1, 246, 165, 20, 20, "left L3 pedicle")
        self.btn = anat.Anatomy.osso_generico(tab1, 182, 168, 20, 20, "right transverse L3 process")
        self.btn = anat.Anatomy.osso_generico(tab1, 266, 167, 20, 20, "left transverse L3 process")
        self.btn = anat.Anatomy.vertebra(tab1, 225, 212, 20, 20, "L4")
        self.btn = anat.Anatomy.organ_generico(tab1, 209, 434, 20, 20, "urinary bladder")
        self.btn = anat.Anatomy.organ_generico(tab1, 173, 307, 20, 20, "right ureter")
        self.btn = anat.Anatomy.organ_generico(tab1, 276, 315, 20, 20, "left ureter")
        self.btn = anat.Anatomy.espaco_articular(tab1, 298, 327, 20, 20, "sacroiliac joint")
        self.btn = anat.Anatomy.organ_generico(tab1, 104, 190, 20, 20, "intestine")
        self.btn = anat.Anatomy.organ_generico(tab1, 351, 178, 20, 20, "intestine")

        self.btn = anat.Anatomy.organ_generico(tab1, 209, 350, 20, 20, "uterus", "")

        self.btn = anat.Anatomy.organ_generico(tab2, 85, 14, 20, 20, "liver")
        self.btn = anat.Anatomy.organ_generico(tab2, 375, 5, 20, 20, "spleen")
        self.btn = anat.Anatomy.osso_generico(tab2, 375, 5, 20, 20, "11th left rib")
        self.btn = anat.Anatomy.organ_generico(tab2, 138, 90, 20, 20, "right kidney")
        self.btn = anat.Anatomy.organ_generico(tab2, 308, 103, 20, 20, "left kidney")
        self.btn = anat.Anatomy.organ_generico(tab2, 153, 201, 20, 20, "right psoas muscle")
        self.btn = anat.Anatomy.organ_generico(tab2, 290, 207, 20, 20, "left psoas muscle")
        self.btn = anat.Anatomy.osso_generico(tab2, 221, 95, 20, 20, "spinous process of L1")
        self.btn = anat.Anatomy.osso_generico(tab2, 204, 166, 20, 20, "right pedicle of L3")
        self.btn = anat.Anatomy.osso_generico(tab2, 246, 165, 20, 20, "left L3 pedicle")
        self.btn = anat.Anatomy.osso_generico(tab2, 182, 168, 20, 20, "right transverse L3 process")
        self.btn = anat.Anatomy.osso_generico(tab2, 266, 167, 20, 20, "left transverse L3 process")
        self.btn = anat.Anatomy.vertebra(tab2, 225, 212, 20, 20, "L4")
        self.btn = anat.Anatomy.organ_generico(tab2, 209, 434, 20, 20, "urinary bladder")
        self.btn = anat.Anatomy.organ_generico(tab2, 173, 307, 20, 20, "right ureter")
        self.btn = anat.Anatomy.organ_generico(tab2, 276, 315, 20, 20, "left ureter")
        self.btn = anat.Anatomy.espaco_articular(tab2, 298, 327, 20, 20, "sacroiliac joint")
        self.btn = anat.Anatomy.organ_generico(tab2, 104, 190, 20, 20, "intestine")
        self.btn = anat.Anatomy.organ_generico(tab2, 351, 178, 20, 20, "intestine")

        self.btn = anat.Anatomy.espaco_articular(tab1, 123, 430, 20, 20, "right hip joint")
        self.btn = anat.Anatomy.espaco_articular(tab1, 318, 432, 20, 20, "left hip joint")


        dic_img = {"xrd75.png": tab1,
                   "xrd76.png": tab2,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_urografia(wx.Panel):
    """Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_urografia, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP Noted")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "AP")
        tab2.SetBackgroundColour("black")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        self.btn = anat.Anatomy.organ_generico(tab1, 174, 44, 20, 20, "right kidney")
        self.btn = anat.Anatomy.organ_generico(tab2, 137, 104, 20, 20, "right kidney")

        self.btn = anat.Anatomy.organ_generico(tab1, 346, 36, 20, 20, "left kidney")
        self.btn = anat.Anatomy.organ_generico(tab2, 293, 84, 20, 20, "left kidney")

        self.btn = anat.Anatomy.organ_generico(tab1, 193, 123, 20, 20, "right ureter")
        self.btn = anat.Anatomy.organ_generico(tab2, 169, 213, 20, 20, "right ureter")

        self.btn = anat.Anatomy.organ_generico(tab1, 315, 92, 20, 20, "left ureter")
        self.btn = anat.Anatomy.organ_generico(tab2, 265, 176, 20, 20, "left ureter")

        self.btn = anat.Anatomy.organ_generico(tab1, 262, 403, 20, 20, "urinary bladder")
        self.btn = anat.Anatomy.organ_generico(tab2, 215, 422, 20, 20, "urinary bladder")


        dic_img = {"xrd77.png": tab1,
                   "xrd130.ipn": tab2,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_osso_nasais(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_osso_nasais, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "Lateral")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Super lower")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Occipito Mental")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.osso_generico(tab1, 248, 261, 20, 20, "nasal bone body")

        self.btn = anat.Anatomy.osso_generico(tab2, 215, 137, 20, 20, "right nasal bone")
        self.btn = anat.Anatomy.osso_generico(tab2, 289, 136, 20, 20, "left nasal bone")

        self.btn = anat.Anatomy.osso_generico(tab1, 272, 216, 20, 20, "frontonasal suture")

        self.btn = anat.Anatomy.osso_generico(tab1, 245, 410, 20, 20, "anterior nasal spine of the maxilla")

        self.btn = anat.Anatomy.parte_mole(tab2, 242, 27, 20, 20, "soft part of the nose")

        dic_img = {"xrd131.ipn": tab1,
                   "xrd132.ipn": tab2,
                   "xrd133.ipn": tab3,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_cranio(wx.Panel):
    """Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_cranio, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Angulation of 15 PA")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "View of Townes")

        tab4 = MyTabPanel(notebook)
        notebook.AddPage(tab4, "Lateral")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.forame(tab1, 295, 95, 20, 20, "sagittal suture")
        self.btn = anat.Anatomy.forame(tab2, 281, 105, 20, 20, "sagittal suture")

        self.btn = anat.Anatomy.forame(tab2, 230, 184, 20, 20, "right lambdoid suture")
        self.btn = anat.Anatomy.forame(tab2, 348, 191, 20, 20, "left lambdoid suture")


        self.btn = anat.Anatomy.osso_generico(tab1, 233, 179, 20, 20, "frontal bone on the right")
        self.btn = anat.Anatomy.osso_generico(tab1, 357, 181, 20, 20, "left frontal bone")

        self.btn = anat.Anatomy.osso_generico(tab1, 303, 292, 20, 20, "crest galli")
        self.btn = anat.Anatomy.osso_generico(tab2, 277, 205, 20, 20, "crest galli")

        self.btn = anat.Anatomy.osso_generico(tab1, 230, 279, 20, 20, "upper margin of the right orbit")
        self.btn = anat.Anatomy.osso_generico(tab2, 197, 228, 20, 20, "upper margin of the right orbit")

        self.btn = anat.Anatomy.osso_generico(tab1, 380, 281, 20, 20, "upper margin of the left orbit")
        self.btn = anat.Anatomy.osso_generico(tab2, 346, 229, 20, 20, "upper margin of the left orbit")

        self.btn = anat.Anatomy.osso_generico(tab1, 233, 345, 20, 20, "inferior right orbit rim")
        self.btn = anat.Anatomy.osso_generico(tab1, 385, 346, 20, 20, "inferior left orbit rim")

        self.btn = anat.Anatomy.osso_generico(tab1, 228, 298, 20, 20, "right petrous bone")
        self.btn = anat.Anatomy.osso_generico(tab2, 170, 292, 20, 20, "right petrous bone")

        self.btn = anat.Anatomy.osso_generico(tab1, 373, 305, 20, 20, "left petrous bone")
        self.btn = anat.Anatomy.osso_generico(tab2, 379, 307, 20, 20, "left petrous bone")


        self.btn = anat.Anatomy.seio_nasal(tab1, 265, 273, 20, 20, "right frontal sinus")
        self.btn = anat.Anatomy.seio_nasal(tab1, 332, 279, 20, 20, "left frontal sinus")

        self.btn = anat.Anatomy.seio_nasal(tab1, 275, 313, 20, 20, "right ethmoidal sinus")
        self.btn = anat.Anatomy.seio_nasal(tab1, 325, 315, 20, 20, "left ethmoid sinus")



        dic_img = {"xrd82.ipn": tab1,
                   "xrd83.ipn": tab2,
                   "xrd84.ipn": tab3,
                   "xrd85.ipn": tab4,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_ossos_da_face(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_ossos_da_face, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "PA 30 °")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Occipito Mental")

        tab4 = MyTabPanel(notebook)
        notebook.AddPage(tab4, "Occipito Mental 30 °")

        tab5 = MyTabPanel(notebook)
        notebook.AddPage(tab5, "Lateral")

        tab6 = MyTabPanel(notebook)
        notebook.AddPage(tab6, "Submentovertex")

        tab7 = MyTabPanel(notebook)
        notebook.AddPage(tab7, "Occipito Mental")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        dic_img = {"xrd86.ipn": tab1,
                   "xrd87.ipn": tab2,
                   "xrd88.ipn": tab3,
                   "xrd89.ipn": tab4,
                   "xrd90.ipn": tab5,
                   "xrd91.ipn": tab6,
                   "xrd92.ipn": tab7,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_seios_da_face(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_seios_da_face, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "PA 30 °")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Lateral")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.forame(tab1, 280, 104, 20, 20, "sagittal suture")
        self.btn = anat.Anatomy.forame(tab2, 294, 108, 20, 20, "sagittal suture")

        self.btn = anat.Anatomy.forame(tab1, 227, 183, 20, 20, "right lambdoid suture")
        self.btn = anat.Anatomy.forame(tab1, 343, 190, 20, 20, "left lambdoid suture")

        self.btn = anat.Anatomy.osso_generico(tab1, 201, 131, 20, 20, "frontal bone on the right")
        self.btn = anat.Anatomy.osso_generico(tab1, 364, 128, 20, 20, "left frontal bone")

        self.btn = anat.Anatomy.osso_generico(tab1, 274, 238, 20, 20, "crest galli")
        self.btn = anat.Anatomy.osso_generico(tab2, 287, 214, 20, 20, "crest galli")

        self.btn = anat.Anatomy.osso_generico(tab1, 198, 229, 20, 20, "upper margin of the right orbit")
        self.btn = anat.Anatomy.osso_generico(tab2, 199, 200, 20, 20, "upper margin of the right orbit")

        self.btn = anat.Anatomy.osso_generico(tab1, 352, 231, 20, 20, "upper margin of the left orbit")
        self.btn = anat.Anatomy.osso_generico(tab2, 374, 201, 20, 20, "upper margin of the left orbit")

        self.btn = anat.Anatomy.osso_generico(tab1, 204, 338, 20, 20, "inferior right orbit rim")
        self.btn = anat.Anatomy.osso_generico(tab2, 193, 312, 20, 20, "inferior right orbit rim")

        self.btn = anat.Anatomy.osso_generico(tab1, 362, 341, 20, 20, "inferior left orbit rim")
        self.btn = anat.Anatomy.osso_generico(tab2, 376, 314, 20, 20, "inferior left orbit rim")

        self.btn = anat.Anatomy.osso_generico(tab1, 170, 306, 20, 20, "right petrous bone")
        self.btn = anat.Anatomy.osso_generico(tab2, 172, 337, 20, 20, "right petrous bone")

        self.btn = anat.Anatomy.osso_generico(tab1, 378, 307, 20, 20, "left petrous bone")
        self.btn = anat.Anatomy.osso_generico(tab2, 400, 342, 20, 20, "left petrous bone")

        self.btn = anat.Anatomy.seio_nasal(tab1, 255, 237, 20, 20, "right frontal sinus")
        self.btn = anat.Anatomy.seio_nasal(tab2, 272, 170, 20, 20, "right frontal sinus")
        self.btn = anat.Anatomy.seio_nasal(tab3, 345, 54, 20, 20, "frontal sinus")

        self.btn = anat.Anatomy.seio_nasal(tab1, 204, 365, 20, 20, "right maxillary sinus")
        self.btn = anat.Anatomy.seio_nasal(tab1, 334, 359, 20, 20, "left maxillary sinus")
        self.btn = anat.Anatomy.seio_nasal(tab3, 313, 177, 20, 20, "maxillary sinus")

        self.btn = anat.Anatomy.seio_nasal(tab1, 296, 239, 20, 20, "left frontal sinus")
        self.btn = anat.Anatomy.seio_nasal(tab2, 314, 172, 20, 20, "left frontal sinus")

        self.btn = anat.Anatomy.seio_nasal(tab1, 246, 298, 20, 20, "right ethmoidal sinus")
        self.btn = anat.Anatomy.seio_nasal(tab2, 264, 291, 20, 20, "right ethmoidal sinus")

        self.btn = anat.Anatomy.seio_nasal(tab1, 302, 300, 20, 20, "left ethmoid sinus")
        self.btn = anat.Anatomy.seio_nasal(tab2, 298, 292, 20, 20, "left ethmoid sinus")

        self.btn = anat.Anatomy.septo(tab1, 272, 376, 20, 20, "nasal septum")
        self.btn = anat.Anatomy.septo(tab2, 285, 362, 20, 20, "nasal septum")

        self.btn = anat.Anatomy.cavidade_nasal(tab3, 194, 209, 20, 20, "cavum")

        self.btn = anat.Anatomy.cavidade_nasal(tab1, 250, 373, 20, 20, "right nasal concha")
        self.btn = anat.Anatomy.cavidade_nasal(tab1, 295, 378, 20, 20, "left nasal concha")

        self.btn = anat.Anatomy.osso_generico(tab3, 367, 98, 20, 20, "nasal bone")

        dic_img = {
            "xrd86.ipn": tab1,
            "xrd87.ipn": tab2,
            "xrd90.ipn": tab3,
            }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_cavum(wx.Panel):
    """Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_cavum, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "Cavum")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.cavidade_nasal(tab1, 187, 257, 20, 20, "cavum")
        self.btn = anat.Anatomy.cavidade_nasal(tab1, 190, 324, 20, 20, "epiglottis")


        dic_img = {"xrd90.ipn": tab1,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_mandibula(wx.Panel):
    """Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_mandibula, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "PA")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Oblíqua")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "Lateral")

        tab4 = MyTabPanel(notebook)
        notebook.AddPage(tab4, "Ortopantograma")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.osso_generico(tab1, 248, 288, 20, 20, "jaw body")
        self.btn = anat.Anatomy.osso_generico(tab2, 327, 312, 20, 20, "jaw body")
        self.btn = anat.Anatomy.osso_generico(tab3, 231, 300, 20, 20, "jaw body")

        self.btn = anat.Anatomy.osso_generico(tab1, 191, 90, 20, 20, "right condyle of the mandible")
        self.btn = anat.Anatomy.osso_generico(tab1, 444, 93, 20, 20, "left condyle of the mandible")

        self.btn = anat.Anatomy.osso_generico(tab3, 133, 104, 20, 20, "mandible condyle")

        self.btn = anat.Anatomy.osso_generico(tab2, 97, 170, 20, 20, "mandible condyle")

        self.btn = anat.Anatomy.osso_generico(tab2, 141, 343, 20, 20, "jaw angle")
        self.btn = anat.Anatomy.osso_generico(tab3, 148, 271, 20, 20, "jaw angle")

        self.btn = anat.Anatomy.osso_generico(tab1, 205, 121, 20, 20, "right coronoid process of the mandible")
        self.btn = anat.Anatomy.osso_generico(tab1, 439, 118, 20, 20, "left coronoid process of the mandible")

        self.btn = anat.Anatomy.osso_generico(tab2, 238, 171, 20, 20, "coronoid process of the mandible")
        self.btn = anat.Anatomy.osso_generico(tab3, 226, 134, 20, 20, "coronoid process of the mandible")

        self.btn = anat.Anatomy.osso_generico(tab1, 217, 188, 20, 20, "right jaw ramus")
        self.btn = anat.Anatomy.osso_generico(tab1, 428, 188, 20, 20, "left jaw ramus")

        self.btn = anat.Anatomy.osso_generico(tab2, 181, 298, 20, 20, "jaw ramus")
        self.btn = anat.Anatomy.osso_generico(tab3, 144, 212, 20, 20, "jaw ramus")

        self.btn = anat.Anatomy.osso_generico(tab1, 322, 343, 20, 20, "jaw symphysis")

        self.btn = anat.Anatomy.osso_generico(tab2, 415, 299, 20, 20, "mentonian protuberance")
        self.btn = anat.Anatomy.osso_generico(tab3, 334, 362, 20, 20, "mentonian protuberance")


        dic_img = {"xrd93.ipn": tab1,
                   "xrd94.ipn": tab2,
                   "xrd95.ipn": tab3,
                   "xrd96.ipn": tab4,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_atm(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_atm, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "Oblíquo Lateral - Boca Fechada")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Oblíquo Lateral - Boca Aberta")

        tab3 = MyTabPanel(notebook)
        notebook.AddPage(tab3, "ATM - Máquina OPG")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        # Gerenciamento da anatomia
        self.btn = anat.Anatomy.espaco_articular(tab1, 109, 159, 20, 20, "temporomandibular joint")

        self.btn = anat.Anatomy.espaco_articular(tab1, 107, 187, 20, 20, "mandible condyle")

        dic_img = {"xrd97.ipn": tab1,
                   "xrd98.ipn": tab2,
                   "xrd99.ipn": tab3,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_transito_intestinal(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_transito_intestinal, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        dic_img = {"xrd100.ipn": tab1,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_enema_opaco(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_enema_opaco, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)
        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        dic_img = {"xrd101.ipn": tab1,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_dacriocistografia(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_dacriocistografia, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)

        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Draw")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        dic_img = {"xrd102.ipn": tab1,
                   "xrd103.ipn": tab2,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_uretrocistografia(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_uretrocistografia, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)

        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "AP")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        dic_img = {"xrd104.ipn": tab1,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_histerossalpingografia(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_histerossalpingografia, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)

        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "Histerossalpingografia")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        dic_img = {"xrd105.ipn": tab1,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_uretrocistografia_retrograda_e_miccional(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_uretrocistografia_retrograda_e_miccional, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)

        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "Uretrocistografia Retrograda e Miccional")

        tab2 = MyTabPanel(notebook)
        notebook.AddPage(tab2, "Uretrocistografia Miccional")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        dic_img = {"xrd106.ipn": tab1,
                   "xrd104.ipn": tab2,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


class MyPanel_img_esofago_estomago_e_duodeno_contrastado(wx.Panel):
    """Meu Panel"""
    def __init__(self, parent, id=wx.ID_ANY):
        """Initialize class attributes."""
        super(MyPanel_img_esofago_estomago_e_duodeno_contrastado, self).__init__(parent, id=wx.ID_ANY)

    def criar_btn(self):

        self.SetBackgroundColour("white")

        # Notebook Tab
        notebook = wx.Notebook(self)

        tab1 = MyTabPanel(notebook)
        notebook.AddPage(tab1, "Contrastado")

        # Gerenciador de Layout
        vSizer = wx.BoxSizer(wx.VERTICAL)
        vSizer.Add(notebook, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(vSizer)

        dic_img = {"xrd107.ipn": tab1,
                   }

        # Imagem tap 1 PA Lombar
        for key, value in dic_img.items():
            torax_img_pa1 = wx.Image(key).ConvertToBitmap()
            self.image = wx.StaticBitmap(value, bitmap=torax_img_pa1, pos=wx.DefaultPosition)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class MyFrame(wx.Frame):
    """Frame"""
    def __init__(self, parent, title=""):
        """Initialize class attributes."""
        super(MyFrame, self).__init__(parent, title=title, size=(1200, 620),
                                      style=wx.DEFAULT_FRAME_STYLE)
        self.url = "https://www.peteralexandercharles.com/"
        self.num = 0
        self.tipo_fra1 = ""
        self.tipo_fra2 = ""
        self.ultimo_texto_label = ""
        self.texto_template = ""

        # Tamanho minimo para a janela
        self.SetMinClientSize((260, 300))
        self.Center()

        # Set Icon
        ico = wx.Icon("xrd108.ipn")
        self.SetIcon(ico)

        # Gerenciador de Layout Horizontal
        self.hSizer = wx.BoxSizer()

        # Gerenciador de Layout Vertical (Principal)
        vSizer = wx.BoxSizer(wx.VERTICAL)

        # Gerencidor de Layout vertical do panel
        self.vSizer_panel_info = wx.BoxSizer(wx.VERTICAL)

        # Setar panel info
        self.panel_info = info_pw.MyPanel_info(self)
        self.vSizer_panel_info.Add(self.panel_info, 0, wx.EXPAND)
        self.hSizer.Add(self.vSizer_panel_info, 1, wx.EXPAND)

        # Setar panel de seleção panel widget torax
        self.panel_widget_torax = MyPanel_img_torax(self)

        # Criar object
        self.panel_widget_coluna_lombar = MyPanel_img_coluna_lombar(self)
        self.panel_widget_coluna_cervical = MyPanel_img_coluna_cervical(self)
        self.panel_widget_coluna_toracica = MyPanel_img_coluna_toracica(self)
        self.panel_widget_coluna_toracolombar = MyPanel_img_coluna_toracolombar(self)
        self.panel_widget_coluna_lombossacra = MyPanel_img_coluna_lombar(self)
        self.panel_widget_coluna_sacrococcix = MyPanel_img_coluna_sacrococcix(self)
        self.panel_widget_coluna_total = MyPanel_img_coluna_total(self)
        self.panel_widget_ombro_direito = MyPanel_img_ombro(self)
        self.panel_widget_ombro_esquerdo = MyPanel_img_ombro(self)
        self.panel_widget_mao_direita = MyPanel_img_mao(self)
        self.panel_widget_mao_esquerda = MyPanel_img_mao(self)
        self.panel_widget_mao_idade_ossea_masc = MyPanel_img_mao_idade_ossea_masc(self)
        self.panel_widget_mao_idade_ossea_fem = MyPanel_img_mao_idade_ossea_fem(self)
        self.panel_widget_dedos_mao_direita = MyPanel_img_mao(self)
        self.panel_widget_dedos_mao_esquerda = MyPanel_img_mao(self)
        self.panel_widget_arcos_costais_direita = MyPanel_img_arcos_costais(self)
        self.panel_widget_arcos_costais_esquerda = MyPanel_img_arcos_costais(self)
        self.panel_widget_clavicula_direita = MyPanel_img_clavicula(self)
        self.panel_widget_clavicula_esquerda = MyPanel_img_clavicula(self)
        self.panel_widget_escapula_direita = MyPanel_img_escapula(self)
        self.panel_widget_escapula_esquerda = MyPanel_img_escapula(self)
        self.panel_widget_punho_direito = MyPanel_img_punho(self)
        self.panel_widget_punho_esquerdo = MyPanel_img_punho(self)
        self.panel_widget_antebraco_direito = MyPanel_img_antebraco(self)
        self.panel_widget_antebraco_esquerdo = MyPanel_img_antebraco(self)
        self.panel_widget_cotovelo_direito = MyPanel_img_cotovelo(self)
        self.panel_widget_cotovelo_esquerdo = MyPanel_img_cotovelo(self)
        self.panel_widget_braco_direito = MyPanel_img_braco(self)
        self.panel_widget_braco_esquerdo = MyPanel_img_braco(self)
        self.panel_widget_bacia = MyPanel_img_bacia(self)
        self.panel_widget_quadril_direito = MyPanel_img_bacia(self)
        self.panel_widget_quadril_esquerdo = MyPanel_img_bacia(self)
        self.panel_widget_coxa_direita = MyPanel_img_bacia(self)
        self.panel_widget_coxa_esquerda = MyPanel_img_bacia(self)
        self.panel_widget_femur_direito = MyPanel_img_femur(self)
        self.panel_widget_femur_esquerdo = MyPanel_img_femur(self)
        self.panel_widget_joelho_direito = MyPanel_img_joelho(self)
        self.panel_widget_joelho_direito_com_carga = MyPanel_img_joelho(self)
        self.panel_widget_joelho_direito_com_axial_de_patela = MyPanel_img_joelho(self)
        self.panel_widget_joelho_esquerdo = MyPanel_img_joelho(self)
        self.panel_widget_joelho_esquerdo_com_carga = MyPanel_img_joelho(self)
        self.panel_widget_joelho_esquerdo_com_axial_de_patela = MyPanel_img_joelho(self)
        self.panel_widget_perna_direita = MyPanel_img_perna(self)
        self.panel_widget_perna_esquerda = MyPanel_img_perna(self)
        self.panel_widget_tornozelo_direito = MyPanel_img_tornozelo(self)
        self.panel_widget_tornozelo_esquerdo = MyPanel_img_tornozelo(self)
        self.panel_widget_pe_direito = MyPanel_img_pe(self)
        self.panel_widget_pe_esquerdo = MyPanel_img_pe(self)
        self.panel_widget_calcaneo_direito = MyPanel_img_calcaneo(self)
        self.panel_widget_calcaneo_esquerdo = MyPanel_img_calcaneo(self)
        self.panel_widget_abdomen_simples = MyPanel_img_abdomen(self)
        self.panel_widget_abdomen_agudo = MyPanel_img_abdomen(self)
        self.panel_widget_urografia = MyPanel_img_urografia(self)
        self.panel_widget_osso_nasais = MyPanel_img_osso_nasais(self)
        self.panel_widget_cranio = MyPanel_img_cranio(self)
        self.panel_widget_ossos_da_face = MyPanel_img_ossos_da_face(self)
        self.panel_widget_seios_da_face = MyPanel_img_seios_da_face(self)
        self.panel_widget_cavum = MyPanel_img_cavum(self)
        self.panel_widget_mandibula = MyPanel_img_mandibula(self)
        self.panel_widget_atm = MyPanel_img_atm(self)
        self.panel_widget_transito_intestinal = MyPanel_img_transito_intestinal(self)
        self.panel_widget_enema_opaco = MyPanel_img_enema_opaco(self)
        self.panel_widget_dacriocistografia = MyPanel_img_dacriocistografia(self)
        self.panel_widget_uretrocistografia = MyPanel_img_uretrocistografia_retrograda_e_miccional(self)
        self.panel_widget_uretrocistografia_retrograda_e_miccional = MyPanel_img_uretrocistografia_retrograda_e_miccional(self)
        self.panel_widget_uretrocistografia_miccional = MyPanel_img_uretrocistografia_retrograda_e_miccional(self)
        self.panel_widget_histerossalpingografia = MyPanel_img_histerossalpingografia(self)
        self.panel_widget_esofago_estomago_e_duodeno_contrastado = MyPanel_img_esofago_estomago_e_duodeno_contrastado(self)

        # One time Class to self
        self.list_panel_img = [self.panel_widget_coluna_lombar,
                         self.panel_widget_coluna_lombossacra,
                         self.panel_widget_coluna_cervical,
                         self.panel_widget_coluna_toracica,
                         self.panel_widget_coluna_toracolombar,
                         self.panel_widget_coluna_sacrococcix,
                         self.panel_widget_coluna_total,
                         self.panel_widget_ombro_direito,
                         self.panel_widget_ombro_esquerdo,
                         self.panel_widget_mao_direita,
                         self.panel_widget_mao_esquerda,
                         self.panel_widget_arcos_costais_direita,
                         self.panel_widget_arcos_costais_esquerda,
                         self.panel_widget_torax,
                         self.panel_widget_clavicula_direita,
                         self.panel_widget_clavicula_esquerda,
                         self.panel_widget_escapula_direita,
                         self.panel_widget_escapula_esquerda,
                         self.panel_widget_dedos_mao_direita,
                         self.panel_widget_dedos_mao_esquerda,
                         self.panel_widget_punho_direito,
                         self.panel_widget_punho_esquerdo,
                         self.panel_widget_antebraco_direito,
                         self.panel_widget_antebraco_esquerdo,
                         self.panel_widget_cotovelo_direito,
                         self.panel_widget_cotovelo_esquerdo,
                         self.panel_widget_braco_direito,
                         self.panel_widget_braco_esquerdo,
                         self.panel_widget_bacia,
                         self.panel_widget_quadril_direito,
                         self.panel_widget_quadril_esquerdo,
                         self.panel_widget_coxa_direita,
                         self.panel_widget_coxa_esquerda,
                         self.panel_widget_femur_direito,
                         self.panel_widget_femur_esquerdo,
                         self.panel_widget_joelho_direito,
                         self.panel_widget_joelho_direito_com_carga,
                         self.panel_widget_joelho_direito_com_axial_de_patela,
                         self.panel_widget_joelho_esquerdo,
                         self.panel_widget_joelho_esquerdo_com_carga,
                         self.panel_widget_joelho_esquerdo_com_axial_de_patela,
                         self.panel_widget_perna_direita,
                         self.panel_widget_perna_esquerda,
                         self.panel_widget_tornozelo_direito,
                         self.panel_widget_tornozelo_esquerdo,
                         self.panel_widget_pe_direito,
                         self.panel_widget_pe_esquerdo,
                         self.panel_widget_calcaneo_direito,
                         self.panel_widget_calcaneo_esquerdo,
                         self.panel_widget_abdomen_simples,
                         self.panel_widget_abdomen_agudo,
                         self.panel_widget_urografia,
                         self.panel_widget_osso_nasais,
                         self.panel_widget_cranio,
                         self.panel_widget_ossos_da_face,
                         self.panel_widget_seios_da_face,
                         self.panel_widget_cavum,
                         self.panel_widget_mandibula,
                         self.panel_widget_atm,
                         self.panel_widget_transito_intestinal,
                         self.panel_widget_enema_opaco,
                         self.panel_widget_dacriocistografia,
                         self.panel_widget_uretrocistografia,
                         self.panel_widget_histerossalpingografia,
                         self.panel_widget_uretrocistografia_retrograda_e_miccional,
                         self.panel_widget_uretrocistografia_miccional,
                         self.panel_widget_esofago_estomago_e_duodeno_contrastado,
                         self.panel_widget_mao_idade_ossea_masc,
                         self.panel_widget_mao_idade_ossea_fem,
                              ]

        # Setar panel img generici
        for item in self.list_panel_img:
            self.hSizer.Add(item, 1, wx.EXPAND)
            item.Hide()

        # lembrar qual estava ligado e titulo do exame
        self.panel_ligado = self.panel_widget_torax
        self.titulo_exame = temp_txt.tp_chest().split("\n", 1)[0]

        # Setar Panel Editor de Texto
        self.panel_text = MyPanel_text_editor(self)
        self.vSizer_panel_info.Add(self.panel_text, 1, wx.EXPAND)

        try:
            filename = "fonte.json"
            with open(filename, "r") as file_object:
                fonte_dados_list = json.load(file_object)
                fonte_str = fonte_dados_list[0]
                size_fonte = fonte_dados_list[1]
                fonte = wx.Font(wx.FontInfo(size_fonte).FaceName(fonte_str))
                self.panel_text.text_editor.SetFont(fonte)
                self.panel_info.nome_paciente_text_ctrl.SetFont(fonte)

        except:
            print("ERRO Fonte")
            pass

        # Setar Panel Informação
        self.panel_clinico = MyPanel_info_clinica(self)
        self.hSizer.Add(self.panel_clinico, 1, wx.EXPAND)
        self.panel_clinico.Hide()

        # StatusBar
        statusBar = self.CreateStatusBar()

        # Criando uma self.toolbar
        tool_img = wx.Image("xrd109.png").ConvertToBitmap()
        mic_img = wx.Image("xrd113.ipn").ConvertToBitmap()
        copy_img = wx.Image("xrd122.ipn").ConvertToBitmap()
        indent_img = wx.Image("xrd114.ipn").ConvertToBitmap()
        resize_img = wx.Image("xrd111.ipn").ConvertToBitmap()
        idea_img = wx.Image("xrd119.ipn").ConvertToBitmap()
        codigo_para_texto_img = wx.Image("xrd123.ipn").ConvertToBitmap()
        codigo_em_texto_img = wx.Image("xrd124.ipn").ConvertToBitmap()

        trocar_frase_img = wx.Image("xrd110.ipn").ConvertToBitmap()
        exchange_img = wx.Image("xrd120.ipn").ConvertToBitmap()
        font_selecton_img = wx.Image("xrd134.png").ConvertToBitmap()
        key_img = wx.Image("donation_img.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        youtube_img = wx.Image("xrd142.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        information_ico = wx.Image("xrd137.ipn").ConvertToBitmap()

        self.toolbar = self.CreateToolBar()
        self.tool_img = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=tool_img, shortHelpString="Toolbar",
longHelpString="Advanced system for radiographic report generation.")
        self.toolbar.AddSeparator()
        self.mic_tool_ico = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=mic_img, shortHelpString="Speech Recognition",
                              longHelpString="Speak to start converting from voice to text.")
        self.copy_ico = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=copy_img,
shortHelpString="Copy report", longHelpString="Click to copy formatted report"
                                         "then it's just paste where"
                                         "vyou wish.")
        self.resut_concl = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=indent_img, shortHelpString="Result:\nConclusion:\nIdeal Text Packing for single report.",
longHelpString="Format the text by placing the report between Result and Conclusion.")
        self.resize = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=resize_img, shortHelpString="Expand text editor",
longHelpString ="Click to expand the text editor and click again to return to normal.")



        self.toolbar.AddSeparator()
        self.codigo_para_texto = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=codigo_para_texto_img, shortHelpString="Here you can create codes for your custom phrases and templates",
                                                       longHelpString="Here you can create codes for your custom phrases and templates.")

        self.codigo_em_texto = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=codigo_em_texto_img, shortHelpString="Clicking here you transform your code into text.",
                                                     longHelpString="Clicking here you transform your code into text.")
        self.toolbar.AddSeparator()

        self.trocar_frase_auto = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=trocar_frase_img, shortHelpString="Here you can replace the standard X-Ray Assistant phrases with yours.",
                                                     longHelpString="Here you can replace the standard X-Ray Assistant phrases with yours.")

        self.trocar_template_auto = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=exchange_img, shortHelpString="Here you can customize the default templates of your X-Ray Assistant.",
                                                     longHelpString="Here you can customize the default templates of your X-Ray Assistant.")

        self.toolbar.AddSeparator()



        self.font_size_selecton = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=font_selecton_img, shortHelpString="Define font type and size",
                                                        longHelpString="Define font type and size")

        self.toolbar.AddSeparator()
        self.youtube_tool = self.toolbar.AddSimpleTool(wx.ID_ANY, bitmap=youtube_img, shortHelpString="Watch a video about it on YouTube!\nWhen the icon gets active.",
                                                  longHelpString="Additional content for you to learn more about this subject on YouTube.")
        self.id_do_youtube_tool = self.youtube_tool.GetId()
        self.toolbar.EnableTool(self.id_do_youtube_tool, False)

        self.toolbar.AddSeparator()
        self.donation_tool = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=key_img, shortHelpString="Donetion.\nYour donation is welcome and helps support the project.",
                                                        longHelpString="Your donation is welcome and helps support the project.")

        self.toolbar.AddStretchableSpace()
        self.info_desenvolvedor = self.toolbar.AddSimpleTool(wx.NewId(), bitmap=information_ico, shortHelpString="",
                                                     longHelpString="")




        self.toolbar.Realize()

        #Set Sizer
        vSizer.Add(self.hSizer, 1, wx.EXPAND)
        self.SetSizer(vSizer)

        # Transparencia
        self.SetTransparent(250)

        # Maximize
        self.Maximize(False)

        # Bind
        # Fala para texto icone microfone
        self.Bind(wx.EVT_TOOL, self.fala_para_texto, self.mic_tool_ico)

        # Fala para texto botão físico: Precionar
        self.panel_text.text_editor.Bind(wx.EVT_KEY_DOWN, self.on_press_gravar)

        # Pegar nome do paciente e colocar no editor de texto:
        self.Bind(wx.EVT_TEXT, self.on_ao_digitar_nome, self.panel_info.nome_paciente_text_ctrl)

        # seleção do relatório template pardão
        self.panel_info.Bind(wx.EVT_MENU, self.on_menu)

        # copiar relatório
        self.Bind(wx.EVT_TOOL, self.on_copiar, self.copy_ico)

        # Add código para texto
        self.Bind(wx.EVT_TOOL, self.on_add_codigo, self.codigo_para_texto)

        # Add texto personal
        self.Bind(wx.EVT_TOOL, self.on_add_texto_personal, self.trocar_frase_auto)

        # Add template personal
        self.Bind(wx.EVT_TOOL, self.on_add_template_personal, self.trocar_template_auto)

        # Font Size Selection Seleção rapida do tamanho da fonte
        self.Bind(wx.EVT_TOOL, self.on_font_size_selecton, self.font_size_selecton)

        # Ao clicar ser abrir no navegador url referente ao assunto
        self.Bind(wx.EVT_TOOL, self.on_abrir_no_navegador_video, self.youtube_tool)

        # Retorna código em texto no texto editor
        self.Bind(wx.EVT_TOOL, self.on_codigo_em_texto, self.codigo_em_texto)

        # formatar relatório
        self.Bind(wx.EVT_TOOL, self.resultado_conclusao, self.resut_concl)

        # Exibir informações do desenvolvedor e contato.
        self.Bind(wx.EVT_TOOL, self.on_info_contato_desenvolvedor, self.info_desenvolvedor)
        self.Bind(wx.EVT_TOOL, self.on_bem_vindo_ico, self.tool_img)

        # Abri Frame para ativar ID
        self.Bind(wx.EVT_TOOL, self.on_patreon, self.donation_tool)

        # Expandir editor de texto
        self.Bind(wx.EVT_TOOL, self.on_resize, self.resize)
        self.flag_resize = True

        # limpar nome do paciente do textCtrl
        self.Bind(wx.EVT_BUTTON, self.on_linpar_nome_pac, self.panel_info.button_clear)
        #self.panel_widget_torax.Bind(wx.EVT_MENU, self.on_menu_rx)

        for item in self.list_panel_img:
            item.Bind(wx.EVT_MENU, self.on_menu_rx)

        # limpar texto do editor de texto
        self.Bind(wx.EVT_BUTTON, self.on_limpar_texto, self.panel_info.apagar_texto)

        # Posição do mouse
        self.panel_widget_torax.Bind(wx.EVT_MOUSEWHEEL, self.on_mouse_pos)


        for item in self.list_panel_img:
            item.Bind(wx.EVT_MOUSEWHEEL, self.on_mouse_pos)

        # Ligar e desligar panel de informação clínica
        # DESATIVADO
#        self.Bind(wx.EVT_TOOL, self.on_idea, self.idea)
        self.idea_flag = False

        # Bind maximizar para refresh
        self.Bind(wx.EVT_MAXIMIZE, self.on_maximize)

        # Panel para ligar e desligar
        self.dic_panel_info = {
            self.panel_info.menu_item_cranio: [temp_txt.tp_skull, self.panel_widget_cranio],
            self.panel_info.menu_item_seios_da_face: [temp_txt.tp_sinuses_of_face, self.panel_widget_seios_da_face],
            self.panel_info.menu_item_cavum: [temp_txt.tp_cavum, self.panel_widget_cavum],
            self.panel_info.menu_item_ossos_da_face: [temp_txt.tp_facial_bone, self.panel_widget_ossos_da_face],
            self.panel_info.menu_item_ossos_nasais: [temp_txt.tp_nasal_bone, self.panel_widget_osso_nasais],
            self.panel_info.menu_item_mandibula: [temp_txt.tp_jaw, self.panel_widget_mandibula],
            self.panel_info.menu_item_atm: [temp_txt.tp_temporomandibular_joints, self.panel_widget_atm],
            self.panel_info.menu_item_coluna_cervical: [temp_txt.tp_cervical_spine, self.panel_widget_coluna_cervical, self.panel_widget_torax],
            self.panel_info.menu_item_coluna_toracica: [temp_txt.tp_thoracic_spine, self.panel_widget_coluna_toracica],
            self.panel_info.menu_item_coluna_toraco_lombar: [temp_txt.tp_thoracic_lumbar_spine, self.panel_widget_coluna_toracolombar],
            self.panel_info.menu_item_coluna_lombar: [temp_txt.tp_lumbar_spine, self.panel_widget_coluna_lombar, self.panel_widget_torax],
            self.panel_info.menu_item_coluna_lombossacra: [temp_txt.tp_lumbosacral_spine, self.panel_widget_coluna_lombossacra],
            self.panel_info.menu_item_coluna_sacro_coccigea: [temp_txt.tp_sacrum_cocix_column, self.panel_widget_coluna_sacrococcix],
            self.panel_info.menu_item_coluna_total: [temp_txt.tp_total_column, self.panel_widget_coluna_total],
            self.panel_info.menu_item_torax: [temp_txt.tp_chest, self.panel_widget_torax],
            self.panel_info.menu_item_arcos_costais_a_direita: [temp_txt.tp_right_costal_arches, self.panel_widget_arcos_costais_direita],
            self.panel_info.menu_item_arcos_costais_a_esquerda: [temp_txt.tp_left_costal_arches, self.panel_widget_arcos_costais_esquerda],
            self.panel_info.menu_item_abdomen_simples: [temp_txt.tp_abdomen_simple, self.panel_widget_abdomen_simples],
            self.panel_info.menu_item_abdome_agudo_simples: [temp_txt.tp_simple_acute_abdome, self.panel_widget_abdomen_agudo],
            self.panel_info.menu_item_articulacoes: [temp_txt.tp_joint, None],
            self.panel_info.menu_item_ombro_direito: [temp_txt.tp_right_shoulder, self.panel_widget_ombro_direito],
            self.panel_info.menu_item_ombro_esquerdo: [temp_txt.tp_left_shoulder, self.panel_widget_ombro_esquerdo],
            self.panel_info.menu_item_clavicula_direita: [temp_txt.tp_right_clavicle, self.panel_widget_clavicula_direita],
            self.panel_info.menu_item_clavicula_esquerda: [temp_txt.tp_left_clavicle, self.panel_widget_clavicula_esquerda],
            self.panel_info.menu_item_escapula_direita: [temp_txt.tp_right_scapular, self.panel_widget_escapula_direita],
            self.panel_info.menu_item_escapula_esquerda: [temp_txt.tp_left_scapular, self.panel_widget_escapula_esquerda],
            self.panel_info.menu_item_braco_direito: [temp_txt.tp_right_arm, self.panel_widget_braco_direito],
            self.panel_info.menu_item_braco_esquerdo: [temp_txt.tp_left_arm, self.panel_widget_braco_esquerdo],
            self.panel_info.menu_item_cotovelo_direito: [temp_txt.tp_right_elbow, self.panel_widget_cotovelo_direito],
            self.panel_info.menu_item_cotovelo_esquerdo: [temp_txt.tp_left_elbow, self.panel_widget_cotovelo_esquerdo],
            self.panel_info.menu_item_antebraco_direito: [temp_txt.tp_right_forearm, self.panel_widget_antebraco_direito],
            self.panel_info.menu_item_antebraco_esquerdo: [temp_txt.tp_left_forearm, self.panel_widget_antebraco_esquerdo],
            self.panel_info.menu_item_punho_direito: [temp_txt.tp_right_wrist, self.panel_widget_punho_direito],
            self.panel_info.menu_item_punho_esquerdo: [temp_txt.tp_left_wrist, self.panel_widget_punho_esquerdo],
            self.panel_info.menu_item_dedos_da_mao_direita: [temp_txt.tp_right_hand_finger, self.panel_widget_dedos_mao_direita],
            self.panel_info.menu_item_dedos_da_mao_esquerda: [temp_txt.tp_left_hand_finger, self.panel_widget_dedos_mao_esquerda],
            self.panel_info.menu_item_mao_direita: [temp_txt.tp_right_hand, self.panel_widget_mao_direita],
            self.panel_info.menu_item_mao_esquerda: [temp_txt.tp_left_hand, self.panel_widget_mao_esquerda],
            self.panel_info.menu_item_bacia: [temp_txt.tp_basin, self.panel_widget_bacia],
            self.panel_info.menu_item_quadril_direito: [temp_txt.tp_right_hip, self.panel_widget_quadril_direito],
            self.panel_info.menu_item_quadril_esquerdo: [temp_txt.tp_left_hip, self.panel_widget_quadril_esquerdo],
            self.panel_info.menu_item_femur_direito: [temp_txt.tp_right_femur, self.panel_widget_femur_direito],
            self.panel_info.menu_item_femur_esquerdo: [temp_txt.tp_left_femur, self.panel_widget_femur_esquerdo],
            self.panel_info.menu_item_coxa_direita: [temp_txt.tp_right_lame_femoral, self.panel_widget_coxa_direita],
            self.panel_info.menu_item_coxa_esquerda: [temp_txt.tp_left_lame_femoral, self.panel_widget_coxa_esquerda],
            self.panel_info.menu_item_joelho_direito: [temp_txt.tp_right_knee, self.panel_widget_joelho_direito],
            self.panel_info.menu_item_joelho_direito_com_carga: [temp_txt.tp_right_knee_with_load, self.panel_widget_joelho_direito_com_carga],
            self.panel_info.menu_item_joelho_direito_com_axial_de_patela: [temp_txt.tp_right_knee_x_ray_with_axial_patella, self.panel_widget_joelho_direito_com_axial_de_patela],
            self.panel_info.menu_item_joelho_esquerdo: [temp_txt.tp_left_knee, self.panel_widget_joelho_esquerdo],
            self.panel_info.menu_item_joelho_esquerdo_com_carga: [temp_txt.tp_left_knee_x_ray_with_load, self.panel_widget_joelho_esquerdo_com_carga],
            self.panel_info.menu_item_joelho_esquerdo_com_axial_de_patela: [temp_txt.tp_left_knee_x_ray_with_axial_patella, self.panel_widget_joelho_esquerdo_com_axial_de_patela],
            self.panel_info.menu_item_perna_direita: [temp_txt.tp_right_leg, self.panel_widget_perna_direita],
            self.panel_info.menu_item_perna_esquerda: [temp_txt.tp_left_leg, self.panel_widget_perna_esquerda],
            self.panel_info.menu_item_tornozelo_direito: [temp_txt.tp_right_ankle, self.panel_widget_tornozelo_direito],
            self.panel_info.menu_item_tornozelo_esquerdo: [temp_txt.tp_left_ankle, self.panel_widget_tornozelo_esquerdo],
            self.panel_info.menu_item_pe_direito: [temp_txt.tp_right_foot, self.panel_widget_pe_direito],
            self.panel_info.menu_item_pe_esquerdo: [temp_txt.tp_left_foot, self.panel_widget_pe_esquerdo],
            self.panel_info.menu_item_calcaneo_direito: [temp_txt.tp_right_calcaneus, self.panel_widget_calcaneo_direito],
            self.panel_info.menu_item_calcaneo_esquerdo: [temp_txt.tp_left_calcaneus, self.panel_widget_calcaneo_esquerdo],
            self.panel_info.menu_item_urografia_excretora: [temp_txt.tp_excretory_urography, self.panel_widget_urografia],
            self.panel_info.menu_item_transito_intestinal: [temp_txt.tp_intestinal_transit, self.panel_widget_transito_intestinal],
            self.panel_info.menu_item_esofago_estomago_e_duodeno_contrastado: [temp_txt.tp_stomach_esophagus_and_contrasted_duodenum, self.panel_widget_esofago_estomago_e_duodeno_contrastado],
            self.panel_info.menu_item_enema_opaco: [temp_txt.tp_enema_opaco, self.panel_widget_enema_opaco],
            self.panel_info.menu_item_dacriocistografia: [temp_txt.tp_dacryocystography, self.panel_widget_dacriocistografia],
            self.panel_info.menu_item_uretrocistografia_miccional: [temp_txt.tp_mictional_urethrocystography, self.panel_widget_uretrocistografia],
            self.panel_info.menu_item_uretrocistografia_retrograda: [temp_txt.tp_retrograde_and_mictional_uretrocystography, self.panel_widget_uretrocistografia_miccional],
            self.panel_info.menu_item_uretrocistografia_retrograda_e_miccional: [temp_txt.tp_retrograde_and_mictional_uretrocystography, self.panel_widget_uretrocistografia_retrograda_e_miccional],
            self.panel_info.menu_item_histerossalpingografia: [temp_txt.tp_hysterossalpingography, self.panel_widget_histerossalpingografia],
            self.panel_info.menu_item_mao_para_idade_ossea_masc: [temp_txt.tp_hand_x_ray_for_bone_age, self.panel_widget_mao_idade_ossea_masc],
            self.panel_info.menu_item_mao_para_idade_ossea_fem: [temp_txt.tp_hand_x_ray_for_bone_age_she, self.panel_widget_mao_idade_ossea_fem],
            self.panel_info.menu_item_escanometria: [temp_txt.tp_scanometry, None],
            self.panel_info.menu_item_legg_calve_perthes_pelve: [temp_txt.tp_legg_calve_perthes_pelve, None],
        }

    # Complemento de controle e entradas
        self.controle_fala_para_texto = False
        self.c = 0

    # Contar arquivos
        self.contar_arquivos()

    # Checkar e criar arquivos memo caso não tenha
        self.on_criar_arquivos_memo()

    # Contador de arquivos
    def contar_arquivos(self):
        """Função para contar os arquivos
        originais."""
        list_xrd_ipn = [
            "xrd1.jpg",
            "xrd1-1.jpg",
            "xrd2.jpg",
            "xrd2-2.jpg",
            "xrd3.jpg",
            "xrd3-3.jpg",
            "xrd4.jpg",
            "xrd4_cerv_.jpg",
            "xrd5.jpg",
            "xrd6.jpg",
            "xrd7.jpg",
            "xrd8.jpg",
            "xrd9.jpg",
            "xrd10.jpg",
            "xrd11.jpg",
            "xrd12.jpg",
            "xrd13.jpg",
            "xrd14.jpg",
            "xrd15.jpg",
            "xrd16.jpg",
            "xrd17.jpg",
            "xrd18.jpg",
            "xrd19.png",
            "xrd20.png",
            "xrd21.png",
            "xrd22.png",
            "xrd23.png",
            "xrd24.png",
            "xrd25.png",
            "xrd26.png",
            "xrd27.png",
            "xrd28.png",
            "xrd29.png",
            "xrd30.png",
            "xrd31.png",
            "xrd32.png",
            "xrd33.png",
            "xrd34.png",
            "xrd35.png",
            "xrd36.png",
            "xrd37.png",
            "xrd38.png",
            "xrd42.png",
            "xrd43.png",
            "xrd44.png",
            "xrd45.png",
            "xrd46.png",
            "xrd47.png",
            "xrd48.png",
            "xrd49.png",
            "xrd50.png",
            "xrd51.png",
            "xrd52.png",
            "xrd53.png",
            "xrd54.png",
            "xrd55.png",
            "xrd56.png",
            "xrd57.png",
            "xrd58.png",
            "xrd59.png",
            "xrd60.png",
            "xrd61.png",
            "xrd62.png",
            "xrd63.png",
            "xrd64.png",
            "xrd65.png",
            "xrd66.png",
            "xrd67.png",
            "xrd68.png",
            "xrd69.png",
            "xrd71.png",
            "xrd72.png",
            "xrd73.png",
            "xrd74.png",
            "xrd75.png",
            "xrd76.png",
            "xrd77.png",
            "xrd130.ipn",
            "xrd131.ipn",
            "xrd132.ipn",
            "xrd133.ipn",
            "xrd82.ipn",
            "xrd83.ipn",
            "xrd84.ipn",
            "xrd85.ipn",
            "xrd86.ipn",
            "xrd87.ipn",
            "xrd88.ipn",
            "xrd89.ipn",
            "xrd90.ipn",
            "xrd91.ipn",
            "xrd92.ipn",
            "xrd93.ipn",
            "xrd94.ipn",
            "xrd95.ipn",
            "xrd96.ipn",
            "xrd97.ipn",
            "xrd98.ipn",
            "xrd99.ipn",
            "xrd100.ipn",
            "xrd101.ipn",
            "xrd102.ipn",
            "xrd103.ipn",
            "xrd104.ipn",
            "xrd105.ipn",
            "xrd106.ipn",
            "xrd107.ipn",
        ]

        for item in list_xrd_ipn:
            try:
                with open(item) as fileobject:
                    n = fileobject
            except FileNotFoundError:
                print("Arquivos faltando!")
                self.Hide()
                msg = wx.MessageBox("Arquivos do programa em falta.\n\nContate a Cosmo Radiology pelo WhatsApp (41)98444-9186 para atendimento!\n\nSite: https://www.peteralexandercharles.com/", "Arquivos do programa em falta.")
                self.Destroy()




    # Criar arquivos para a memória e custommizar

    def on_criar_arquivos_memo(self):
        """Função para checar e criar arquivos
        de customização  caso necessário
        antes da inicialização."""

        list_de_check = [
            "xrd78.ipn",
            "xrd79.ipn",
            "xrd80.ipn",
        ]

        for item in list_de_check:
            try:
                with open(item, "r") as fileobject:
                    n = fileobject
                    print("Arquivo já existe: " + item)

            except FileNotFoundError:
                with open(item, "w") as fileobject:
                    print("Criado: " + item)
                    list_dics = [{"rx123": "memo dic template personalizado criado"}]
                    json.dump(list_dics, fileobject)


    # Pegar posição do mouse
    def on_mouse_pos(self, event):
        """Pegar posição do mouse."""
        pos = event.GetPosition()
        c = self.c
        c += 1
        self.c = c
        print(c, ">>> " + str(pos[0] - 18), end="")
        print(", " + str(pos[1] - 38) + ",")
        print("-*"*5)

    def fala_para_texto(self, event):
        """Converter fala para texto."""
        if self.controle_fala_para_texto == False:
            self.controle_fala_para_texto = True
            wx.adv.Sound("star_mic_sound.wav").Play()
            thread.start_new_thread(self.fala_para_texto_thread, (1, ))

    def fala_para_texto_thread(self, meuId):
        wx.adv.Sound("star_mic_sound.wav").Play()
        print("Pronto para ouvir!")
        try:

            while True:
                texto_falado = FalaParaTexto.audio_para_texto(None)
                if texto_falado in ["sair", "sai", "parar",]:
                    wx.adv.Sound("stop_snd.wav").Play()
                    self.controle_fala_para_texto = False
                    print("Okay goodbye!")
                    exit()
                else:
                    self.controle_fala_para_texto = True
                    print(texto_falado)
                    # Para o texto sair em maiúscula somente no início.
                    pos = self.panel_text.text_editor.GetInsertionPoint()
                    pos_bool_linha_coluna = self.panel_text.text_editor.PositionToXY(pos)
                    print("GetInsertionPointLine:", self.panel_text.text_editor.PositionToXY(pos))
                    pos_coluna = pos_bool_linha_coluna[1]
                    pos_linha = pos_bool_linha_coluna[2]

                    # se em maiuscula manter conformidade
                    linha_do_insertion_point = self.panel_text.text_editor.GetLineText(pos_linha)
                    print("Linha lida: " + linha_do_insertion_point)

                    try:
                        if texto_falado != None:
                            print(texto_falado)

                            # Pontuação
                            texto_falado = texto_falado.replace("vírgula", ", ")
                            texto_falado = texto_falado.replace("ponto final", ". ")
                            texto_falado = texto_falado.replace("Ponto Final", ". ")
                            texto_falado = texto_falado.replace("Ponto final", ". ")
                            texto_falado = texto_falado.replace("ponto-final", ". ")
                            texto_falado = texto_falado.replace("nova linha", "\n")
                            texto_falado = texto_falado.replace("galinha", "\n")
                            texto_falado = texto_falado.replace("remover", "#remover#")
                            texto_falado = texto_falado.replace("REMOVER", "#remover#")

                            texto_falado = texto_falado.replace("espaço", " ")
                            texto_falado = texto_falado.replace("dois pontos", ": ")

                            # Ajustes e correções de acordo com o contexto
                            texto_falado = texto_falado.replace("Coincidência ", "Com incidência ")
                            texto_falado = texto_falado.replace("Coincidências ", "Com incidências ")
                            texto_falado = texto_falado.replace("coincidência ", "com incidência ")
                            texto_falado = texto_falado.replace("coincidências ", "com incidências ")

                            texto_falado = texto_falado.replace("Na topografia ", "na topografia ")
                            texto_falado = texto_falado.replace("Medial ", "medial ")

                            if pos_coluna == 0:
                                texto_falado = texto_falado[0].title() + texto_falado[1:]

                            if linha_do_insertion_point == linha_do_insertion_point.upper() \
                                    and linha_do_insertion_point.strip() != "":
                                texto_falado = texto_falado.upper()

                            if linha_do_insertion_point.strip() == "Obs.:" \
                                    or linha_do_insertion_point.strip() == "Obs:":
                                texto_falado = texto_falado[0].title() + texto_falado[1:]
                                texto_falado = texto_falado

                            if "\n" in texto_falado or "#remover#" in texto_falado or "#REMOVER#" in texto_falado:
                                print("Code 5403 texto_falado:>>>"+ texto_falado + "<<<")
                                texto_falado = texto_falado.replace("#remover#", "")
                                texto_falado = texto_falado.replace("#REMOVER#", "")
                                self.panel_text.text_editor.WriteText(texto_falado)
                            else:
                                print("Code 5408 texto_falado:>>>" + texto_falado + "<<<")
                                self.panel_text.text_editor.WriteText(texto_falado + " ")

                    except TypeError:
                        print("Verifique sua conexição com a internet.")
                    self.controle_fala_para_texto = True
        except:
            print("Unhandled exception in thread started by (Problema para ouvir)")
            self.controle_fala_para_texto = False
            self.fala_para_texto_thread


    def on_press_gravar(self, event):
        """Ao pressionar o botão de gravar no controle da Philips"""
        keycode = event.GetKeyCode()
        print("keycode:", keycode)
        if keycode == wx.WXK_F1:
            self.fala_para_texto(event)
        event.Skip()


    def on_ao_digitar_nome(self, event):
        """Ao difitar nome passar para editor de texto"""
        print("Digitando!")


    def on_add_codigo(self, event):
        """Ao clicar em adicionar código para texto
        mostrar janelas para o usuário entra com o
        código em seguda com o texto que será associado a ele."""

        janela_codigo_texto = FrameParaCodigos(self)


    def on_add_texto_personal(self, event):
        """Ao clicar em adicionar código para texto
        mostrar janelas para o usuário entra com o
        código em seguda com o texto que será associado a ele."""

        janela_codigo_texto = FrameParaCodigos_Texto(self, text=self.ultimo_texto_label, memo_file="xrd80.ipn")

    def on_add_template_personal(self, event):
        """Ao clicar em adicionar código para texto
        mostrar janelas para o usuário entra com o
        código em seguda com o texto que será associado a ele."""

        janela_codigo_texto = FrameParaCodigos_Template(self, text=self.texto_template, memo_file="xrd78.ipn")

    def on_font_size_selecton(self, event):
        """Ao selecionar o tamanho da fonte mudar no
        seletor Rápido da fonte mudar no editor de texto"""
        dialog = wx.FontDialog(self, wx.FontData())

        if dialog.ShowModal() == wx.ID_OK:
            data = dialog.GetFontData()
            font = data.GetChosenFont()
            colour = data.GetColour()
            print("You selected: %s, %d points\n" % (
                font.GetFaceName(), font.GetPointSize()
            ))
        dialog.Destroy()
        try:
            fonte = wx.Font(font)

        except UnboundLocalError:
            print("Cancelou fonte")

        else:
            self.panel_text.text_editor.SetFont(fonte)
            self.panel_info.nome_paciente_text_ctrl.SetFont(fonte)

            filename = "fonte.json"
            with open(filename, "w") as file_object:
                fonte_str = [fonte.GetFaceName(), fonte.GetPointSize()]
                json.dump(fonte_str, file_object)


    def on_codigo_em_texto(self, event):
        """Ao clicar em código para texto
        nosso código em texto editor se transforma
        em texto."""

        filename = "xrd79.ipn"
        with open(filename, "r") as file_object:
            list_codigo = json.load(file_object)
            for dic in list_codigo:
                print(dic)
                for key, value in dic.items():
                    texto_no_panel = self.panel_text.text_editor.GetValue()
                    codigo_em_texto = texto_no_panel.replace("==" + key, value)
                    self.panel_text.text_editor.SetValue(codigo_em_texto)


    def on_copiar(self, event):
        """Ao clicar no ico copiar, copiar texto do
        editor para área de transferência."""
        print("Pronto para copiar.")
        nome = self.panel_info.nome_paciente_text_ctrl.Value.upper().strip()
        texto = self.panel_text.text_editor.Value

        if nome != "":
            nome += "\n\n"
            texto = nome + self.panel_text.text_editor.Value
        else:
            texto = self.panel_text.text_editor.Value

        data_text_obj = wx.TextDataObject()                     # Cesta para texto
        if wx.TheClipboard.Open() or wx.TheClipboard.IsOpen():  # Abrir área de transferência do pc
            data_text_obj.SetText(texto)                        # Coloco texto na cesta
            wx.TheClipboard.SetData(data_text_obj)              # Coloco cesta na a. de trans
            wx.TheClipboard.Close()                             # Fecho área de trasferência.

    def on_copiar_linha(self, texto_para_copiar):
        """Copiar text_label para a memória
         editor para área de transferência."""
        print("Pronto para copiar.")
        texto = texto_para_copiar
        data_text_obj = wx.TextDataObject()                     # Cesta para texto
        if wx.TheClipboard.Open() or wx.TheClipboard.IsOpen():  # Abrir área de transferência do pc
            data_text_obj.SetText(texto)                        # Coloco texto na cesta
            wx.TheClipboard.SetData(data_text_obj)              # Coloco cesta na a. de trans
            wx.TheClipboard.Close()                             # Fecho área de trasferência.

    def resultado_conclusao(self, event):
        """Formata o texto colocando o relatório entre Resultado e Conclusão."""
        texto = self.panel_text.text_editor.GetValue()
        #print(texto)
        self.panel_text.text_editor.SetValue(self.titulo_exame + "\nRESULTADO:\n" + texto + "\nCONCLUSÃO:\n")

    def on_info_contato_desenvolvedor(self, event):
        """Função para exibir informações do desenvolvedor
        e endereço para contato."""
        texto = """Este programa foi desenvolvido para auxiliar os médicos radiologistas na realização precisa e ágil dos relatórios radiográficos. 

Desenvolvedor: Dr. Pedro Alexandre Camilo de Oliveira 
Programador e Médico. 
Telefone e WhatsApp para contato: (31) 991704644 
Site: https://www.peteralexandercharles.com/ 

Dúvidas, adequação do software para sua empresa, entre em contato. 

Excelentes relatórios!"""
        # info_para_cliente = wx.MessageBox(texto, "Desenvolvedor")
        frame_apre = MyFrame_Apresentacao(self)

    def on_key_tool(self, event):
        """Função para mostra a janela de ativação
        da ID."""
        frame = MyFrame_Key(self)
        frame.Center()

    def on_bem_vindo_ico(self, event):
        """Função para mostrar mensagem de boas-vindas e
        contado do desenvolvedor."""
        texto = """Bem-vindo ao Assistente Raio-X! 

Este programa foi cuidadosamente desenvolvido para auxiliá-lo na realização precisa e ágil de relatórios radiográficos. 

Suporta conversão de fala em texto, template gerados automaticamente para os mais diversos exames, seleção dos itens no template, e muito mais! 

Sinta-se à vontade para entrar em conosco! 
Telefone e WhatsApp: (31) 991704644

Site: https://www.peteralexandercharles.com/"""
        # message_box = wx.MessageBox(texto, "Assistente Raio-X")
        frame_apre = MyFrame_Apresentacao(self, img_name="wallpaperflare.com_wallpaper-_8_.png")

    def on_patreon(self, event):
        """Patreon web page."""
        MyFrame_Apresentacao(self, img_name="patreon_img.png",
                             url="https://www.patreon.com/docfaster", url_label="                              https://www.patreon.com/docfaster                              ")

    def on_linpar_nome_pac(self, event):
        """Limpar nome do paciente do TextCtrl."""
        text = ""
        self.panel_info.nome_paciente_text_ctrl.SetValue(text)


    def on_limpar_texto(self, event):
        """Limpar editor de texto."""
        try:
            if self.panel_text.text_editor.Value != "":
                self.texto_guardado = self.panel_text.text_editor.GetValue()
                self.panel_text.text_editor.SetValue("")
            elif self.panel_text.text_editor.Value == "":
                self.panel_text.text_editor.SetValue(self.texto_guardado)
        except AttributeError:
            print("Mensagem: Editor de texto vazio.")


    def on_menu(self, event):
        event_id = event.GetId()
        event_obj = event.EventObject

    # Coloca o texto
        for key, value in self.dic_panel_info.items():
            try:
                desligar = value[1].Hide()
                value[1].DestroyChildren()
            except AttributeError:
                print("Falta implementar panel com imagem e ocutar os demais")
            if event_id == key.GetId():
                texto = value[0]()
                texto_add = texto
                self.texto_template = texto_add

                self.titulo_exame = value[0]().split("\n", 1)[0]

                # Novo Template personalizado se tiver
                filename = "xrd78.ipn"

                try:
                    with open(filename, "r") as file_object:
                        list_dics = json.load(file_object)
                        for dic in list_dics:
                            for key_dic, value_dic in dic.items():
                                print("OK")
                                if value[0]() == key_dic:
                                    print("texto_label TEMPLATE== key TEMPLATE:")
                                    texto = value_dic
                except FileNotFoundError:
                    with open(filename, "w") as file_object:
                        list_dics = [{"rx123": "memo dic template personalizado criado"}]
                        json.dump(list_dics, file_object)

                print("AQUI O TEXTO:\n", texto)
                print("#"*5)

                texto_lista = texto.split("\n")
                dlg_escolha_texto = wx.MultiChoiceDialog(self, "Choose which template you want to put",
                                                         "Template", choices=texto_lista)

                lista_index = []
                cont = 0
                for item in texto_lista:
                    lista_index.append(cont)
                    cont += 1
                dlg_escolha_texto.SetSelections(lista_index)

                modal_texto = dlg_escolha_texto.ShowModal()
                if modal_texto == wx.ID_OK:
                    texto_index = dlg_escolha_texto.GetSelections()
                    texto_add = ""
                    for item in texto_index:
                        texto_add += texto_lista[item]
                        texto_add += "\n"

                elif modal_texto == wx.ID_CANCEL:
                    texto_add = ""

                dlg_escolha_texto.Destroy()
                if texto_add != "":
                    texto_add += "\n"

                self.panel_text.text_editor.AppendText(texto_add)
                self.panel_clinico.texto_info_clinica.SetValue("")
                self.panel_clinico.conclusao_info_clinica.SetValue("")
                img = wx.Image("xrd116.ipn").ConvertToBitmap()
                self.panel_clinico.info_imagem.SetBitmap(img)
                self.panel_clinico.info_imagem.Refresh()
                try:
                    ligar = value[1]
                    ligar.criar_btn()
                    ligar.Show()

                    # Redesenhar para evitar erro.
                    self.panel_info.Refresh()

                    self.panel_ligado = value[1]
                    self.flag_resize = True
                except AttributeError:
                    print("!!!!@@@@")
        self.Layout()

    def on_resize(self, event):
        event_id = event.GetId()
        event_obj = event.EventObject

        """Expandir editor de texto."""
        if self.flag_resize == True:
            self.panel_ligado.Hide()
            self.flag_resize = False
        elif self.flag_resize == False:
            self.panel_ligado.Show()
            self.flag_resize = True
        self.Layout()
        self.panel_clinico.Refresh()
        self.panel_info.Refresh()

    def on_idea(self, event):
        """Mostrar ou esconder o panel de informação
        clínica."""
        if self.idea_flag == False:
            self.panel_clinico.Show()
            self.idea_flag = True
        elif self.idea_flag == True:
            self.panel_clinico.Hide()
            self.idea_flag = False
        self.Layout()
        self.Refresh(eraseBackground=True)

    def on_abrir_no_navegador_video(self, event):
        """Função para abri o url informado
        no navegador de internet só para youtube"""
        print("VOU TENTAR ABRIR!")
        try:
            short_link_youtube = self.webpage.split("/")[3]
            url = "https://www.youtube.com/embed/" + short_link_youtube + "?rel=0&autoplay=1;fs=1;autohide=0;hd=0;"
            wx.LaunchDefaultBrowser(url)
        except IndexError:
            print(self.webpage)
            print("Não foi possivel abrir a pagina")


    def on_maximize(self, event):
        """Redesenhar o quadro ao maximizar"""
        self.Refresh()
        print("Is Maximized:", self.IsMaximized())


    def fun_multiChoice_sem_ponto_final(self, tipo_aorta, escolhas, texto_label, to_replace, join=""):
        # Parte comunitária 1º MultiChoice
        modal_tipo = tipo_aorta.ShowModal()
        if modal_tipo == wx.ID_OK:
            aorta_tipo_select = tipo_aorta.GetSelections()
            aorta_texto = join
            for item in aorta_tipo_select:
                aorta_texto += escolhas[item]
                aorta_texto += ", "
            aorta_texto = aorta_texto[:-2]
            aorta_texto = aorta_texto.replace(" co.", ".")
            aorta_texto = aorta_texto[::-1]
            aorta_texto = aorta_texto.replace(",", "dna ", 1)
            aorta_texto = aorta_texto[::-1].strip()
            texto_label = texto_label.replace(to_replace, aorta_texto)
            return texto_label
            if aorta_texto == ".":
                texto_label = ""
                return texto_label
        elif modal_tipo == wx.ID_CANCEL:
            texto_label = ""
            return texto_label

    def fun_multiChoice_sem_e(self, tipo_aorta, escolhas, texto_label, to_replace, join="", ponto_final=True):
        # Parte comunitária 1º MultiChoice
        modal_tipo = tipo_aorta.ShowModal()
        if modal_tipo == wx.ID_OK:
            aorta_tipo_select = tipo_aorta.GetSelections()
            aorta_texto = join
            for item in aorta_tipo_select:
                aorta_texto += escolhas[item]
                aorta_texto += ", "
            if ponto_final == True:
                aorta_texto = aorta_texto[:-2] + "."
            aorta_texto = aorta_texto.replace(" co.", ".")
            aorta_texto = aorta_texto[::-1]
            #aorta_texto = aorta_texto.replace(",", "dna ", 1)
            aorta_texto = aorta_texto[::-1].strip()
            texto_label = texto_label.replace(to_replace, aorta_texto)
            return texto_label
            if aorta_texto == ".":
                texto_label = ""
                return texto_label
        elif modal_tipo == wx.ID_CANCEL:
            texto_label = ""
            return texto_label


    def fun_multiChoice(self, tipo_aorta, escolhas, texto_label, to_replace, join="", ponto_final=True):
        # Parte comunitária 1º MultiChoice
        modal_tipo = tipo_aorta.ShowModal()
        if modal_tipo == wx.ID_OK:
            aorta_tipo_select = tipo_aorta.GetSelections()
            aorta_texto = join
            for item in aorta_tipo_select:
                aorta_texto += escolhas[item]
                aorta_texto += ", "
            if ponto_final == True:
                aorta_texto = aorta_texto[:-2] + "."
            aorta_texto = aorta_texto.replace(" co.", ".")
            aorta_texto = aorta_texto[::-1]
            aorta_texto = aorta_texto.replace(",", "dna ", 1)
            aorta_texto = aorta_texto[::-1].strip()
            texto_label = texto_label.replace(to_replace, aorta_texto)
            return texto_label
            if aorta_texto == ".":
                texto_label = ""
                return texto_label
        elif modal_tipo == wx.ID_CANCEL:
            texto_label = ""
            return texto_label


    def fun_singleChoice(self, tipo_aorta, escolhas, texto_label, to_replace, join="", ponto_final=True, e=True, virgula=True):
        # Parte comunitária 1º SingleChoice
        # Parte comunitária 1º SingleChoice
        modal_tipo = tipo_aorta.ShowModal()
        if modal_tipo == wx.ID_OK:
            aorta_tipo_select = []
            aorta_tipo_select.append(tipo_aorta.GetSelection())
            aorta_texto = join
            for item in aorta_tipo_select:
                aorta_texto += escolhas[item]
                if virgula == True:
                    aorta_texto += ", "
            if ponto_final == True:
                aorta_texto = aorta_texto[:-2] + "."
            aorta_texto = aorta_texto.replace(" co.", ".")
            aorta_texto = aorta_texto[::-1]
            if e == True:
                aorta_texto = aorta_texto.replace(",", "dna ", 1)
            aorta_texto = aorta_texto[::-1].strip()
            texto_label = texto_label.replace(to_replace, aorta_texto)
            return texto_label
            if aorta_texto == ".":
                texto_label = ""
                return texto_label
        elif modal_tipo == wx.ID_CANCEL:
            texto_label = ""
            return texto_label


    def fun_singleChoice_sem_e(self, tipo_aorta, escolhas, texto_label, to_replace, join="", ponto_final=True, virgula=True):
        # Parte comunitária 1º SingleChoice
        # Parte comunitária 1º SingleChoice
        modal_tipo = tipo_aorta.ShowModal()
        if modal_tipo == wx.ID_OK:
            aorta_tipo_select = []
            aorta_tipo_select.append(tipo_aorta.GetSelection())
            aorta_texto = join
            for item in aorta_tipo_select:
                aorta_texto += escolhas[item]
                if virgula == True:
                    aorta_texto += ", "
            if ponto_final == True:
                aorta_texto = aorta_texto[:-2] + "."
            aorta_texto = aorta_texto.replace(" co.", ".")
            aorta_texto = aorta_texto[::-1]
            aorta_texto = aorta_texto[::-1].strip()
            texto_label = texto_label.replace(to_replace, aorta_texto)
            return texto_label
            if aorta_texto == ".":
                texto_label = ""
                return texto_label
        elif modal_tipo == wx.ID_CANCEL:
            texto_label = ""
            return texto_label

    def text_label_plural(self, text_label):
        """torna as palavras do text_label
        conjugadas no plural."""
        texto = text_label
        texto = texto.replace(" no ", " nos ").replace(" corpo ", " corpos ").replace(" vertebral ", " vertebrais ")\
            .replace(" da ", " das ").replace(" do ", " dos ").replace(" amplitude ", " amplitudes ").replace(" forame ", " forames ")\
            .replace(" nível ", " níveis ").replace(" espaço ", " espaços ").replace(" discal ", " discais ").replace(" imagem ", " imagens ")\
            .replace(" Delimita-se ", " Delimitam-se ").replace(" radiopaca ", " radiopacas ").replace(" projetada ", " projetadas ")\
            .replace(" pequeno ", " pequenos ").replace(" nódulo ", " nódulos ").replace(" pulmonar ", " pulmonares ")\
            .replace("Dispositivo ", "Dispositivos ").replace(" intersomático ", " intersomáticos ")\
            .replace("radiopaca, ", "radiopacas, ").replace("Imagem ", "Imagens ")
        # replace correção
        texto = texto.replace(" projetadas nos terço ", " projetadas no terço ").replace(" dos pulmão ", " do pulmão ")\
            .replace(" a pequenos nódulos pulmonar", " a pequenos nódulos pulmonares")
        return texto


    def text_label_adequar_convencao(self, text_label):
        """torna as palavras do text_label
        conjugadas no plural."""
        texto = text_label
        texto = texto.replace("do compartimento medial do joelho e compartimento lateral do joelho", "femorotibial bicompartimental")
        texto = texto.replace("do compartimento medial do joelho, compartimento lateral do joelho e compartimento femoropatelar", "tricompartimental do joelho")
        texto = texto.replace("do compartimento medial do joelho e compartimento femoropatelar", "do compartimento femorotibial medial e femoropatelar")
        texto = texto.replace("do compartimento lateral do joelho e compartimento femoropatelar", "do compartimento femorotibial lateral e femoropatelar")
        texto = texto.replace("em osteossíntese composta por,", "em osteossíntese composta por")
        texto = texto.replace("íntegros e sem sinais de soltura", ", íntegros e sem sinais de soltura")

        texto = texto.replace("âncoras de sutura ortopédicas em região medular , íntegros e sem sinais de soltura", "âncoras de sutura ortopédicas em região medular, íntegras e sem sinais de soltura")
        texto = texto.replace("âncoras de sutura ortopédicas , íntegros e sem sinais de soltura", "âncoras de sutura ortopédicas, íntegras e sem sinais de soltura")

        texto = texto.replace("com , caracterizada", ", caracterizada")
        texto = texto.replace("ao base", "a base")
        texto = texto.replace("irregularidade subcondral e esclerose subcondral", "irregularidade e esclerose subcondrais")

        # evitar repetição
        texto = texto.replace("com espessamento mucoso, com formação de nível hidroaéreo", "com espessamento mucoso, formação de nível hidroaéreo")

        # singular dos materiais
        texto = texto.replace("0 fios de Kirschner", "fio de Kirschner")
        texto = texto.replace("1 fios de Kirschner", "um fio de Kirschner")

        texto = texto.replace("0 fios de Kirschner em região medular", "fio de Kirschner em região medular")
        texto = texto.replace("1 fios de Kirschner em região medular", "um fio de Kirschner em região medular")

        texto = texto.replace("0 pinos de Steinmann", "pino de Steinmann")
        texto = texto.replace("1 pinos de Steinmann", "um pino de Steinmann")

        texto = texto.replace("0 pinos de Steinmann em região medular", "pino de Steinmann em região medular")
        texto = texto.replace("1 pinos de Steinmann em região medular", "um pino de Steinmann em região medular")

        texto = texto.replace("0 placas de fixação metálica parafusadas", "placa de fixação metálica parafusada")
        texto = texto.replace("1 placas de fixação metálica parafusadas", "uma placa de fixação metálica parafusada")

        texto = texto.replace("0 hastes bloqueadas no canal medular", "haste bloqueada no canal medular")
        texto = texto.replace("1 hastes bloqueadas no canal medular", "uma hastes bloqueadas no canal medular")

        texto = texto.replace("0 âncoras de sutura ortopédicas", "âncora de sutura ortopédica")
        texto = texto.replace("1 âncoras de sutura ortopédicas", "uma âncora de sutura ortopédica")

        texto = texto.replace("0 âncoras de sutura ortopédicas em região medular", "âncora de sutura ortopédica em região medular")
        texto = texto.replace("1 âncoras de sutura ortopédicas em região medular", "uma âncora de sutura ortopédica em região medular")

        texto = texto.replace("0 materiais de alta densidade", "material de alta densidade")
        texto = texto.replace("1 materiais de alta densidade", "material de alta densidade")

        texto = texto.replace("0 parafusos de atenuação metálica", "parafuso de atenuação metálica")
        texto = texto.replace("1 parafusos de atenuação metálica", "um parafuso de atenuação metálica")

        texto = texto.replace("0 prótese glenoumeral", "prótese glenoumeral")
        texto = texto.replace("1 prótese glenoumeral", "prótese glenoumeral")

        texto = texto.replace("#descrever_material_em_fratura_sim_não#", "")
        texto = texto.replace("#descrever_material_em_fratura_tipos#", "")
        texto = texto.replace("#descrever_tipo_de_osteossíntese#", "")
        texto = texto.replace("#descrever_integridade_material#", "")
        texto = texto.replace("#descrever_fratura_em_corpo_vertebral_sim_não#", "")
        texto = texto.replace("#descrever_fratura_em_corpo_vertebral_quantidade#", "")
        texto = texto.replace("#descrever_locais_rinofaringe#", "")
        texto = texto.replace("#descrever_associação_sinusite#", "")
        texto = texto.replace("#descrever_locais_seios_da_face#", "")

        return texto

    # Escrever texto para o editor do panel_widget_torax
        # estou dando prioridade para a helpstring

    def on_menu_rx(self, event):
        """Escrever texto para o editor estou dando prioridade para a helpstring"""
        event_id = event.GetId()
        event_obj = event.EventObject

        self.label_item = event_obj.GetLabel(event_id)

        if event_obj.GetHelpString(event_id) == "":
            texto_label = event_obj.GetLabel(event_id) + "\n"
            self.ultimo_texto_label = texto_label

            # Desativar link tool do youtube
            self.toolbar.EnableTool(self.id_do_youtube_tool, False)

            filename = "xrd80.ipn"
            try:
                with open(filename, "r") as file_object:
                    list_dics = json.load(file_object)
                    for dic in list_dics:
                        for key, value in dic.items():
                            print("TEXT LABEL:", texto_label)
                            print("Key:", key)
                            if texto_label == key + "\n":
                                print("texto_label == key:")
                                texto_label = value + "\n"
            except FileNotFoundError:
                pass

            self.panel_text.text_editor.WriteText(texto_label)
            #self.on_copiar_linha(texto_label.replace("\n", ""))


        elif event_obj.GetHelpString(event_id).split != "":
            texto_label = event_obj.GetHelpString(event_id).split("#r#")[1]
            self.nome_anat = event_obj.GetTitle()
            nome_anat_ex_lombar = self.nome_anat.split()[0][0].replace("L", "lombar").replace("T", "torácica").replace("S","sacral").replace("C", "cervical")

            self.nome_anat = event_obj.GetTitle().lower()
            self.label = event_obj.GetLabel(event_id).lower()


            # Mecanismo de seleção para fala composta

            # 1º SingleChoice > 2º MultiChoice > Fim

            # 1º SingleChoice
            # Parte individual
            if "#descrever_lesão_ossea_tipo#" in texto_label:
                escolhas = ["Bone injury", "Osteolytic injury", "Radiopaque image", "Miniature radiopaque image"]

                tipo_aorta = wx.SingleChoiceDialog(self, "Describe.", "Description",
                                                  choices=escolhas)
                self.to_replace = "#descrever_lesão_ossea_tipo#"


                # Parte comunitária 1º SingleChoice
                modal_tipo = tipo_aorta.ShowModal()
                if modal_tipo == wx.ID_OK:
                    aorta_tipo_select = []
                    aorta_tipo_select.append(tipo_aorta.GetSelection())
                    aorta_texto = ""
                    for item in aorta_tipo_select:
                        aorta_texto += escolhas[item]
                        #aorta_texto += escolhas[item]
                        aorta_texto += ", "
                    aorta_texto = aorta_texto[:-2] + ""
                    #aorta_texto = aorta_texto[:-2] + "."
                    #aorta_texto = aorta_texto.replace(" co.", ".")
                    aorta_texto = aorta_texto[::-1]
                    print("AQUI:", aorta_texto)
                    aorta_texto = aorta_texto.replace(",", "dna ", 1)
                    aorta_texto = aorta_texto[::-1].strip()
                    texto_label = texto_label.replace(self.to_replace, aorta_texto)
                elif modal_tipo == wx.ID_CANCEL:
                    texto_label = ""

                # 2º MultiChoice
                # Parte individual
                if "#descrever_lesão_ossea_2#" in texto_label:
                    escolhas = ["expansive", "non-expansive", "benign expansive", "malignant expansive", "",
                                 "with cortical bone destruction", "with regular cortical bone destruction", "without cortical bone destruction", "",
                                 "hypotransparent", "scleroric", "",
                                 "well delimited", "well circumscribed", "poorly delimited", "",
                                 "with narrow transition zone", "with wide transition zone"
                                 "with sclerotic border", "with adjacent reaction sclerosis halo", "",
                                 "no periosteal reaction", "with periosteal reaction", "with benign periosteal reaction", "with aggressive periosteal reaction", "with Codman triangle", ""
                                 "aggressive"]

                    tipo_aorta = wx.MultiChoiceDialog(self, "Describe", "Description",
                                                       choices=escolhas)
                    self.to_replace = "#descrever_lesão_ossea_2#"

                    # Parte comunitária 2º MultiChoice
                    modal_tipo = tipo_aorta.ShowModal()
                    if modal_tipo == wx.ID_OK:
                        aorta_tipo_select = tipo_aorta.GetSelections()
                        aorta_texto = ""
                        for item in aorta_tipo_select:
                            aorta_texto += escolhas[item]
                            aorta_texto += ", "
                        aorta_texto = aorta_texto[:-2] + "."
                        aorta_texto = aorta_texto.replace(" co.", ".")
                        aorta_texto = aorta_texto[::-1]
                        print("AQUI:", aorta_texto)
                        aorta_texto = aorta_texto.replace(",", "dna ", 1)
                        aorta_texto = aorta_texto[::-1].strip()
                        texto_label = texto_label.replace(self.to_replace, aorta_texto)
                    elif modal_tipo == wx.ID_CANCEL:
                        texto_label = ""

            if "#num_medindo#" in texto_label:
                self.num = wx.GetNumberFromUser("What is the measurement in millimeters?", "", "Measure", 0,
                                                0, 100, self,)
                if self.num != -1:
                    texto_label = texto_label.replace("#num_medindo#",
                                                      "measuring approximately " + str(self.num) + " millimeters in diameter,")
                if self.num == -1:
                    texto_label = texto_label.replace("#num_medindo#", "")
                if self.num == 0:
                    texto_label = texto_label.replace(", measuring measuring approximately 0 mm in diameter", "")


            if "#num_medindo_so_num#" in texto_label:
                self.num = wx.GetNumberFromUser("What is the measurement in mm?", "", "Measure", 0,
                                                0, 100, self,)
                if self.num != -1:
                    texto_label = texto_label.replace("#num_medindo_so_num#", str(self.num))


            if "#descrever_luxação_ou_subluxação#" in texto_label:
                escolhas = [
                    "Subluxation", "Dislocation"
                ]
                tipo_aorta = wx.SingleChoiceDialog(self, "If desired, characterize the degree of commitment.", "Degree of commitment", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_luxação_ou_subluxação#", join="", ponto_final=False, e=False, virgula=False)

            if "#variancia_ulnar#" in texto_label:
                escolhas = ["positive",
                     "negative",]
                tipo_aorta = wx.SingleChoiceDialog(self, "What type of ulnar variance?", "Ulnar variance", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#variancia_ulnar#", join="", ponto_final=False, e=False, virgula=False)


            if "#descrever_tipo_de_estudo_radiografico_ex_pos_cirurgico#" in texto_label:
                escolhas = [
                    "",
                     "radiographic study of postoperative evolutionary control, evidence",
                     "radiographic study of post-surgical evolutionary control, evidence",
                     "radiographic study of post-traumatic evolutionary control, evidence",
                     "evolutionary control radiographic study, evidence",
                            ]
                tipo_aorta = wx.SingleChoiceDialog(self, "Characterize the type of radiographic study.", "type of radiographic study", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_tipo_de_estudo_radiografico_ex_pos_cirurgico#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_aspecto_de_fratura_pregressa_consolidada#" in texto_label:
                escolhas = ["fracture sequel",
                     "sequelae aspect of fracture",
                     "consolidated fracture",
                     "consolidation fracture",
                     "signs of ligament reconstruction",
                     "arthroplasty",
                     "longitudinal radiolucent lines",
                     "transverse radiolucent traces",]
                tipo_aorta = wx.SingleChoiceDialog(self, "If desired, characterize the degree of commitment.", "Degree of commitment", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_aspecto_de_fratura_pregressa_consolidada#", join="", ponto_final=False, e=False, virgula=False)


            if "#descrever_material_em_fratura_sim_não#" in texto_label:
                msg_confirmar_material = wx.MessageDialog(self, "Presence of orthopedic fixation material?",
                                                          "Orthopedic fixation material?",
                                                          style=wx.YES_NO|wx.ICON_QUESTION)

                if "#descrever_tipo_de_osteossíntese#" in texto_label:
                    escolhas = ["",
                         "in osteosynthesis composed by",]
                    tipo_aorta = wx.SingleChoiceDialog(self, "If you wish, characterize the osteosynthesis.",
                                                       "Osteossíntese", choices=escolhas)
                    texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label,
                                                        "#descrever_tipo_de_osteossíntese#", join="",
                                                        ponto_final=False, e=False, virgula=False)

                modal_msg_material = msg_confirmar_material.ShowModal()
                if modal_msg_material == wx.ID_YES:
                    print("Material list.")

                    if "#descrever_material_em_fratura_tipos#" in texto_label:
                        escolhas = ["Kirschner wires",
                                     "Kirschner wires in the medullary region",
                                     "Steinmann pins",
                                     "Steinmann pins in the medullary region",
                                     "bolted metal fastening plates",
                                     "rods blocked in the spinal canal",
                                     "orthopedic suture anchors",
                                     "orthopedic suture anchors in the medullary region",
                                     "high density materials",
                                     "metallic attenuation screws",
                                     "glenohumeral prosthesis with intramedullary nail fixed with bone cement",]
                        tipo_aorta = wx.MultiChoiceDialog(self, "Describe", "Description",
                                                          choices=escolhas)

                        texto_label = self.fun_multiChoice_sem_ponto_final(tipo_aorta, escolhas, texto_label,
                                                                 "#descrever_material_em_fratura_tipos#")
                        texto_label = texto_label.replace("#descrever_material_em_fratura_sim_não#", "")

                        print("Sou texto_label:" + texto_label)

                        list_escolhas_mat = tipo_aorta.GetSelections()
                        print("list_escolhas:", list_escolhas_mat)

                        for item_escolhido_mat in list_escolhas_mat:
                            str_item = escolhas[item_escolhido_mat]

                            if str_item in texto_label:
                                self.num = wx.GetNumberFromUser("What is the number of " + str_item + " found?", "",
                                                                str_item, 0,
                                                                0, 100, self)
                                texto_label = texto_label.replace(str_item, str(self.num) + " " + str_item)


                        if "#descrever_integridade_material#" in texto_label:
                            escolhas = ["intact and without signs of release",
                                 "intact and with no sign of release",
                                 "intact and without signs of release",
                                 "complete and with no sign of release",]
                            tipo_aorta = wx.SingleChoiceDialog(self, "If you wish, characterize the osteosynthesis.",
                                                               "Osteosynthesis", choices=escolhas)
                            texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label,
                                                                "#descrever_integridade_material#", join="",
                                                                ponto_final=False, e=False, virgula=False)

                        # Antes de liberar o texto para continuar
                        texto_label = self.text_label_adequar_convencao(texto_label)
                        print("Test local 1: " + texto_label)
                elif modal_msg_material == wx.ID_NO:
                    # Antes de liberar o texto para continuar
                    texto_label = self.text_label_adequar_convencao(texto_label)
                    print("Do not show list")

            if "#descrever_grau_ex_incipientes_plural#" in texto_label:
                escolhas = ["", "incipient", "discrete", "moderate", "accentuated"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If desired, characterize the degree of commitment.", "Degree of commitment", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_ex_incipientes_plural#", join="", ponto_final=False, e=False, virgula=False)


            if "#descrever_grau_ex_incipientes_singular#" in texto_label:
                escolhas = ["", "mild", "fledgling", "discreet", "moderate", "sharp", "important"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If desired, characterize the degree of commitment.", "Degree of commitment", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_ex_incipientes_singular#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_grau_ex_incipientes_singular_masculino#" in texto_label:
                escolhas = ["", "fledgling", "discreet", "moderate", "accentuated", "important"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If desired, characterize the degree of commitment.", "Degree of commitment", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_ex_incipientes_singular_masculino#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_grau_ex_leve_singular_masculino#" in texto_label:
                escolhas = ["", "light", "discreet", "small", "moderate", "sharp", "important"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If desired, characterize the degree of commitment.", "Degree of commitment", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_ex_leve_singular_masculino#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_grau_ex_diminuta_singular_feminino#" in texto_label:
                escolhas = ["", "diminutive", "small", "minimal", "discreet", "accentuated", "important", "exuberant"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If desired, characterize the degree of commitment.", "Degree of commitment", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_ex_diminuta_singular_feminino#", join="", ponto_final=False, e=False, virgula=False)


            if "#descrever_grau_ex_incipientes_plural_masculino#" in texto_label:
                escolhas = ["", "incipient", "discrete", "moderate", "accentuated", "important"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If desired, characterize the degree of commitment.", "Degree of commitment", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_ex_incipientes_plural_masculino#", join="", ponto_final=False, e=False, virgula=False)


            if "#descrever_coxa_profunda_ou_protusa_fundos#" in texto_label:
                escolhas = [
                    "right acetabular fundus",
                     "left acetabular fundus",
                     "acetabular funds",
                ]
                tipo_aorta = wx.SingleChoiceDialog(self, "Describe yourself characterizes deep thigh or protrusion.", "Deep thigh or protrusion", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_coxa_profunda_ou_protusa_fundos#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_coxa_profunda_ou_protusa#" in texto_label:
                escolhas = [", protrudes medially to the ilioischiatic line, featuring deep thigh",
                     ", protrude medially to the ilioischiatic lines, characterizing bilateral deep thigh",
                     "and ipsilateral femoral head, protrude medially to the ilioischiatic line, characterizing protruding thigh",
                     "and femoral heads, protrude medially to the ilioischiatic lines, characterizing bilateral protruding thigh",]
                tipo_aorta = wx.SingleChoiceDialog(self, "Describe yourself characterizes deep thigh or protrusion.", "Deep thigh or protrusion", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_coxa_profunda_ou_protusa#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_numero_reducao_coluna#" in texto_label:
                escolhas = ["at least one of", "some", "multiple", "several"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish, characterize the number of vertebral bodies committed.", "Committed vertebral bodies", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_numero_reducao_coluna#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_fratura_em_corpo_vertebral_sim_não#" in texto_label:
                msg_confirmar_material = wx.MessageDialog(self, "Presence of fracture in any vertebral body?",
                                                          "fracture in any vertebral body?",
                                                          style=wx.YES_NO|wx.ICON_QUESTION)

                modal_msg_material = msg_confirmar_material.ShowModal()
                if modal_msg_material == wx.ID_YES:
                    if "#descrever_fratura_em_corpo_vertebral_quantidade#" in texto_label:
                        escolhas = [
                            "emphasis on reducing the height of one of the vertebral bodies",
                            "emphasis on reducing the height of at least one of the vertebral bodies",
                            "reduction of the height of some of the vertebral bodies",
                            "reduction of the height of several vertebral bodies",
                            "reduction of the height of multiple vertebral bodies",
                        ]
                        tipo_aorta = wx.SingleChoiceDialog(self, "How many approximately?",
                                                           "How many", choices=escolhas)
                        texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label,
                                                            "#descrever_fratura_em_corpo_vertebral_quantidade#", join=" with ",
                                                            ponto_final=False, e=False, virgula=False)

                        # Antes de liberar o texto para continuar
                        texto_label = self.text_label_adequar_convencao(texto_label)
                        print("Test local 1: " + texto_label)
                elif modal_msg_material == wx.ID_NO:
                    # Antes de liberar o texto para continuar
                    texto_label = self.text_label_adequar_convencao(texto_label)
                    print("Do not show list")

            if "#descrever_sugestao_de_exame_coluna#" in texto_label:
                escolhas = ["",
                            "best assessed by specific radiographs",
                             "the findings can be better evaluated by specific radiographs",
                            ]
                tipo_aorta = wx.SingleChoiceDialog(self, "If desired, characterize the degree of commitment.", "Degree of commitment", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_sugestao_de_exame_coluna#", join=", ", ponto_final=False, e=False, virgula=False)

            if "#descrever_osteofitos#" in texto_label:
                escolhas = ["", "fledgling", "exuberant"]
                tipo_aorta = wx.SingleChoiceDialog(self, "Describe osteophytes if you wish.", "Description of osteophytes", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_osteofitos#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_grau_de_redução#" in texto_label:
                escolhas = ["", "mild", "moderate", "sharp", "important"]
                tipo_aorta = wx.SingleChoiceDialog(self, "Describe the degree of space reduction.", "Characterization of the reduction.", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_de_redução#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_fratura_ex_completa#" in texto_label:
                escolhas = [
                    "", "complete", "incomplete"
                ]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish to describe the type of fracture.\nAs for the cortical extension, it is complete or incomplete.", "Describe the type of fracture", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_fratura_ex_completa#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_ex_completas#" in texto_label:
                escolhas = [
                    "", "complete", "incomplete"
                ]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish to describe the type\n.If complete or incomplete.", "Describe the type", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_ex_completas#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_causa_secundaria_da_rarefacao_ossea#" in texto_label:
                escolhas = [
                    "", ", by probable disuse.", ", probably secondary to immobilization."
                ]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish you can describe the possible cause of the observed bone rarefaction.", "Describe bone rarefaction", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_causa_secundaria_da_rarefacao_ossea#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_selecione_local#" in texto_label:
                escolhas = ["", "distal end", "middle-end", "proximal end"]
                tipo_aorta = wx.SingleChoiceDialog(self, "Select the place where you change and find it.", "Select the location", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_selecione_local#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_desvio_direcao#" in texto_label:
                escolhas = ["lateral", "medial", "anterior", "posterior", "inferior", "superior"]
                tipo_aorta = wx.MultiChoiceDialog(self, "Select the direction of the deviation.", "Select the direction of the detour.", choices=escolhas)
                texto_label = self.fun_multiChoice_sem_ponto_final(tipo_aorta, escolhas, texto_label, "#descrever_desvio_direcao#", join="")

            # 1º MultiChoice > 2º MultiChoice > Fim

            # 1º MultiChoice > Fim
            # 1º MultiChoice
            # Parte individual
            if "#descrever_aorta#" in texto_label:
                escolhas = ["extended", "ectasia", "tortuous", "with atheromatous calcifications",
                            "with incipient parietal calcifications", "with parietal calcifications"]
                tipo_aorta = wx.MultiChoiceDialog(self, "Describe the type of aorta.", "Aortic description",
                                                  choices=escolhas)
                texto_label = self.fun_multiChoice(tipo_aorta, escolhas, texto_label, "#descrever_aorta#")
                print("SEE:", texto_label)

            if "#descrever_irregularidade_supeita_de_fratura#" in texto_label:
                escolhas = [
                    "irregularity",
                    "radiolucent trace",
                ]
                tipo_aorta = wx.MultiChoiceDialog(self, "Describe the type of irregularity suspected of fracture.", "suspected fracture irregularity",
                                                  choices=escolhas)
                texto_label = self.fun_multiChoice_sem_ponto_final(tipo_aorta, escolhas, texto_label, "#descrever_irregularidade_supeita_de_fratura#")
                print("VER:", texto_label)

            if "#descrever_irregularidade_cortical_trabeculado#" in texto_label:
                escolhas = ["in the cortical", "in the bone trabecular", "cortical and bony trabecular", "bone"]
                tipo_aorta = wx.SingleChoiceDialog(self, "Describe cortical or bone trabecular irregularity \nthat in the context of trauma may represent a fracture.", "Irregular location", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_irregularidade_cortical_trabeculado#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_no_contexto_de_trauma#" in texto_label:
                escolhas = ["", ", the fracture may correspond.",", the fracture may correspond, given the trauma context.",
                            ", and may correspond to the fracture sequela."]
                tipo_aorta = wx.SingleChoiceDialog(self, "Describe cortical or bone trabecular irregularity \nthat in the context of trauma may represent a fracture.", "Irregular location", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_no_contexto_de_trauma#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_grau_ex_leve#" in texto_label:
                escolhas = ["", "light", "minimal", "small", "moderate", "sharp", "important"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish you can describe the degree.", "Describe the degree", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_ex_leve#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_grau_ex_leves_plural#" in texto_label:
                escolhas = ["", "light", "minimal", "small", "moderate", "accentuated", "important"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish you can describe the degree.", "Describe the degree", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_ex_leves_plural#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_grau_ex_signigicativas_plural#" in texto_label:
                escolhas = ["", "significant", "important", "noteworthy"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish you can describe the degree.", "Describe the degree", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_ex_signigicativas_plural#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_locais_joelho#" in texto_label:
                escolhas = ["medial knee compartment",
                     "lateral knee compartment",
                     "patellofemoral compartment",]
                tipo_aorta = wx.MultiChoiceDialog(self, "Describe which compartment or compartments are compromised.",
                                                  "Knee joint spaces.", choices=escolhas)

                texto_label = self.fun_multiChoice_sem_ponto_final(tipo_aorta, escolhas, texto_label, "#descrever_locais_joelho#", join="")
                if len(tipo_aorta.GetSelections()) > 1:
                    texto_label = self.text_label_adequar_convencao(texto_label)


            if "#descrever_locais_rinofaringe#" in texto_label:
                escolhas = ["from the rhinopharynx",
                     "from cavum",]
                tipo_aorta = wx.MultiChoiceDialog(self, "Describe which compartment or compartments are compromised.",
                                                  "Pharyngeal spaces.", choices=escolhas)

                texto_label = self.fun_multiChoice_sem_ponto_final(tipo_aorta, escolhas, texto_label, "#descrever_locais_rinofaringe#", join="")
                #if len(tipo_aorta.GetSelections()) > 1:
                #    texto_label = self.text_label_adequar_convencao(texto_label)
                texto_label = self.text_label_adequar_convencao(texto_label)

            if "#descrever_locais_seios_da_face#" in texto_label:
                escolhas = ["frontal sinuses",
                     "ethmoidal sinuses",
                     "maxillary sinuses",
                     "sphenoid sinuses",]
                tipo_aorta = wx.MultiChoiceDialog(self, "Describe which compartment or compartments are compromised.",
                                                  "Pharyngeal spaces.", choices=escolhas)

                texto_label = self.fun_multiChoice_sem_ponto_final(tipo_aorta, escolhas, texto_label, "#descrever_locais_seios_da_face#", join=" of ")
                #if len(tipo_aorta.GetSelections()) > 1:
                #    texto_label = self.text_label_adequar_convencao(texto_label)


            if "#descrever_associação_sinusite#" in texto_label:
                escolhas = [
                    "mucous thickening",
                    "with hydro-air level formation",
                ]
                tipo_aorta = wx.MultiChoiceDialog(self, "Describe which compartment or compartments are compromised.",
                                                  "Pharyngeal spaces.", choices=escolhas)

                texto_label = self.fun_multiChoice_sem_ponto_final(tipo_aorta, escolhas, texto_label, "#descrever_associação_sinusite#", join=" e ")
                #if len(tipo_aorta.GetSelections()) > 1:
                #    texto_label = self.text_label_adequar_convencao(texto_label)


            if "#descrever_espaco_art#" in texto_label:
                if "knee" in self.nome_anat or "compartment" in self.nome_anat:
                    escolhas = ["subchondral cysts", "mild subchondral sclerosis of the ipsilateral tibial plateau", "mild subchondral sclerosis of the tibial plateaus", "subchondral sclerosis of the ipsilateral tibial plateau", "subchondral sclerosis of the tibial plateaus",
                                 "subchondral sclerosis of femoral condyles", "subchondral sclerosis of femoral condyles and tibial plateaus", "marginal osteophytes",
                                 "bone irregularity", "presence of intra-articular gas"]

                elif "articulação coxofemoral" in self.nome_anat:
                    escolhas = ["subchondral cysts", "subchondral sclerosis of the acetabular roof", "marginal osteophytes", "bone irregularity",
                                 "presence of intra-articular gas"]

                else:
                    escolhas = ["subchondral cysts", "subchondral sclerosis", "marginal osteophytes", "bone irregularity",
                                 "presence of intra-articular gas"]

                tipo_aorta = wx.MultiChoiceDialog(self, "Describe the joint space.", "Description of the joint space",
                                                  choices=escolhas)
                texto_label = self.fun_multiChoice(tipo_aorta, escolhas, texto_label, "#descrever_espaco_art#", join=" with ")

            if "#descrever_espaco_art_alterações_degenerativas#" in texto_label:
                if "knee" in self.nome_anat:
                    escolhas = ["subchondral cysts", "mild subchondral sclerosis of the ipsilateral tibial plateau", "mild subchondral sclerosis of the tibial plateaus", "subchondral sclerosis of the ipsilateral tibial plateau", "subchondral sclerosis of the tibial plateaus",
                                 "subchondral sclerosis of femoral condyles", "subchondral sclerosis of femoral condyles and tibial plateaus", "marginal osteophytes",
                                 "bone irregularity", "presence of intra-articular gas"]
                else:
                    escolhas = [", characterized by reduced joint space",
                         ", characterized by subchondral irregularity",
                         "subchondral cysts", "subchondral sclerosis",
                         "marginal osteophytes", "bone irregularity",
                         "presence of intra-articular gas"]

                tipo_aorta = wx.MultiChoiceDialog(self, "Describe the joint space.", "Description of the joint space",
                                                  choices=escolhas)
                texto_label = self.fun_multiChoice(tipo_aorta, escolhas, texto_label, "#descrever_espaco_art_alterações_degenerativas#", join=" with ")

                print("Check: " + texto_label)
                texto_label = self.text_label_adequar_convencao(texto_label)



            if "#seleção_vertebra#" in texto_label:
                if self.nome_anat[0] == "c" in texto_label:
                    escolhas = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "T1", "T2"]
                elif self.nome_anat[0] == "t" in texto_label:
                    escolhas = ["C7", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12", "L1"]
                elif self.nome_anat[0] == "l" in texto_label:
                    escolhas = ["T12", "L1", "L2", "L3", "L4", "L5", "S1"]
                elif self.nome_anat[0] == "s" in texto_label:
                    escolhas = ["L5", "S1", "S2", "S3", "S4"]
                tipo_aorta = wx.MultiChoiceDialog(self, "Select the affected vertebrae", "Select the vertebrae",
                                                  choices=escolhas)
                texto_label = self.fun_multiChoice(tipo_aorta, escolhas, texto_label, "#seleção_vertebra#", join="")
                print("len: ",len(tipo_aorta.GetSelections()))
                print(texto_label)
                if len(tipo_aorta.GetSelections()) > 1:
                    texto_label = self.text_label_plural(texto_label)


            if "#seleção_vertebra_sem_ponto#" in texto_label:
                if self.nome_anat[0] == "c" in texto_label:
                    escolhas = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "T1", "T2"]
                elif self.nome_anat[0] == "t" in texto_label:
                    escolhas = ["C7", "T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12", "L1"]
                elif self.nome_anat[0] == "l" in texto_label:
                    escolhas = ["T12", "L1", "L2", "L3", "L4", "L5", "S1"]
                elif self.nome_anat[0] == "s" in texto_label:
                    escolhas = ["L5", "S1", "S2", "S3", "S4"]
                tipo_aorta = wx.MultiChoiceDialog(self, "Select the affected vertebrae", "Select the vertebrae",
                                                  choices=escolhas)
                texto_label = self.fun_multiChoice_sem_ponto_final(tipo_aorta, escolhas, texto_label, "#seleção_vertebra_sem_ponto#", join="")
                print("len: ",len(tipo_aorta.GetSelections()))
                print(texto_label)
                if len(tipo_aorta.GetSelections()) > 1:
                    texto_label = self.text_label_plural(texto_label)



            if "#seleção_espaço_vertebral#" in texto_label:
                if self.nome_anat[0] == "c" in texto_label:
                    escolhas = ["C1-C2", "C2-C3", "C3-C4", "C4-C5", "C5-C6", "C6-C7", "C7-T1", "T1-T2", "T2-T3"]
                elif self.nome_anat[0] == "t" in texto_label:
                    escolhas = ["C7-T1", "T1-T2", "T2-T3", "T3-T4", "T4-T5", "T5-T6", "T6-T7", "T7-T8", "T8-T9", "T9-T10", "T10-T11", "T11-T12", "T12-L1", "L1-L2"]
                elif self.nome_anat[0] == "l" in texto_label:
                    escolhas = ["T12-L1", "L1-L2", "L2-L3", "L3-L4", "L4-L5", "L5-S1", "L4-VT"]
                elif self.nome_anat[0] == "s" in texto_label:
                    escolhas = ["L5-S1", "S1-S2", "S2-S3", "S3-S4", "S4-S5"]
                tipo_aorta = wx.MultiChoiceDialog(self, "Select the vertebral spaces involved", "Select the vertebral spaces",
                                                  choices=escolhas)
                texto_label = self.fun_multiChoice(tipo_aorta, escolhas, texto_label, "#seleção_espaço_vertebral#", join="")
                if len(tipo_aorta.GetSelections()) > 1:
                    texto_label
                    texto_label = self.text_label_plural(texto_label)


            if "#seleção_espaço_vertebral_sem_ponto_final#" in texto_label:
                if self.nome_anat[0] == "c" in texto_label:
                    escolhas = ["C1-C2", "C2-C3", "C3-C4", "C4-C5", "C5-C6", "C6-C7", "C7-T1", "T1-T2", "T2-T3"]
                elif self.nome_anat[0] == "t" in texto_label:
                    escolhas = ["C7-T1", "T1-T2", "T2-T3", "T3-T4", "T4-T5", "T5-T6", "T6-T7", "T7-T8", "T8-T9", "T9-T10", "T10-T11", "T11-T12", "T12-L1", "L1-L2"]
                elif self.nome_anat[0] == "l" in texto_label:
                    escolhas = ["T12-L1", "L1-L2", "L2-L3", "L3-L4", "L4-L5", "L5-S1", "L4-VT"]
                elif self.nome_anat[0] == "s" in texto_label:
                    escolhas = ["L5-S1", "S1-S2", "S2-S3", "S3-S4", "S4-S5"]
                tipo_aorta = wx.MultiChoiceDialog(self, "Select the vertebral spaces involved", "Select the vertebral spaces",
                                                  choices=escolhas)
                texto_label = self.fun_multiChoice_sem_ponto_final(tipo_aorta, escolhas, texto_label, "#seleção_espaço_vertebral_sem_ponto_final#", join="")
                if len(tipo_aorta.GetSelections()) > 1:
                    texto_label
                    texto_label = self.text_label_plural(texto_label)



            if "#descrever_alteracoes_espaco_dis#" in texto_label:
                escolhas = ["marginal osteophytes", "irregularity of the vertebral plateaus",
                             "anterior and posterior osteophyte formation on the periphery of vertebral bodies",
                             "bone irregularity",
                             "bone sclerosis in the vertebral plateaus"]

                tipo_aorta = wx.MultiChoiceDialog(self, "Describe the joint space.", "Description of the joint space", choices=escolhas)
                texto_label = self.fun_multiChoice_sem_ponto_final(tipo_aorta, escolhas, texto_label, "#descrever_alteracoes_espaco_dis#")


            if "#single_hd#" in texto_label:
                escolhas = ["", "unspecific to the method", "of probable osteoporotic origin",
                            "of probable traumatic origin"]

                tipo_aorta = wx.SingleChoiceDialog(self, "diagnostic hypothesis", "diagnostic hypothesis", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#single_hd#", join="")

            if "#descrever_ex_para_a_direita#" in texto_label:
                escolhas = ["to the right", "to the left", ""]
                tipo_aorta = wx.SingleChoiceDialog(self, "Which direction", "Which direction?", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_ex_para_a_direita#", join="", ponto_final=False, virgula=False)

            if "#descrever_ex_a_direita_bilateral#" in texto_label:
                escolhas = ["", "on the right", "on the left", "bilateral"]
                tipo_aorta = wx.SingleChoiceDialog(self, "Which direction?", "Which direction?", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_ex_a_direita_bilateral#", join="", ponto_final=False, virgula=False)

            if "#descrever_ex_a_direita_bilaterais#" in texto_label:
                escolhas = ["", "on the right", "on the left", "bilaterais"]
                tipo_aorta = wx.SingleChoiceDialog(self, "Which direction", "Which direction?", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_ex_a_direita_bilaterais#", join="", ponto_final=False, virgula=False)

            if "#descrever_neoarticulação_sacral#" in texto_label:
                escolhas = ["", "with signs of sacral neoarticulation", "without signs of sacral neoarticulation", "with signs of sacral neoarticulation on the right",
                             ", with signs of left sacral neoarticulation", ", with signs of bilateral sacral neoarticulation"]
                tipo_aorta = wx.SingleChoiceDialog(self, "Is there a sign of sacral neoarticulation?", "sacral neoarticulation", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_neoarticulação_sacral#", join="", ponto_final=False, virgula=False)

            if "#descrever_ex_direita_cobb#" in texto_label:
                escolhas = [
                    "right", "left"
                ]
                tipo_aorta = wx.SingleChoiceDialog(self, "Description of convexity in Cobb angle          \nWhat is the direction of convexity?", "Description of convexity in Cobb angle", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_ex_direita_cobb#", join="", ponto_final=False, virgula=False)

            if "#descrever_ex_direita_halle#" in texto_label:
                escolhas = [
                    "right", "left"
                ]
                tipo_aorta = wx.SingleChoiceDialog(self, "Note air cell on the floor from which it orbits", "Airframe location", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_ex_direita_halle#", join="", ponto_final=False, virgula=False)


            if "#descrever_linha_porte_de_peso#" in texto_label:
                escolhas = [
                    "central", "projecting earlier", "projecting later",
                ]
                tipo_aorta = wx.SingleChoiceDialog(self, "Describe the position of the weight carrying line in relation to the body of S1.", "Weight carrying line", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_linha_porte_de_peso#", join="", ponto_final=False, virgula=False)

            if "#descrever_posicao_osso#" in texto_label:
                escolhas = [
                    "", "designed in soft parts adjacent to the " + self.nome_anat, "designed in soft parts prior to " + self.nome_anat, "designed in soft parts after the " + self.nome_anat, "designed in soft parts laterally to the " + self.nome_anat, "designed in soft parts medially to the " + self.nome_anat]
                tipo_aorta = wx.SingleChoiceDialog(self, "What is the position?", "Position", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_posicao_osso#", join="", ponto_final=False, virgula=False)
                texto_label = self.text_label_adequar_convencao(texto_label)

            if "#descrever_posicao_mole#" in texto_label:
                escolhas = ["", "designed in " + self.nome_anat]
                tipo_aorta = wx.SingleChoiceDialog(self, "What is the position?", "Position", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_posicao_mole#", join="", ponto_final=False, virgula=False)

            if "#descrever_opacidade_imagem#" in texto_label:
                escolhas = ["", "radiopaque", "radiolucent"]
                tipo_aorta = wx.SingleChoiceDialog(self, "What is the opacity of the image?", "Opacity", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_opacidade_imagem#", join="", ponto_final=False, virgula=False)

            if "#descrever_formato_imagem#" in texto_label:
                escolhas = ["rounded",
                     "linear",
                     "oval",
                     "irregular",
                     "rude",
                     "rude",]
                tipo_aorta = wx.SingleChoiceDialog(self, "What is the opacity of the image?", "Opacity", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_formato_imagem#", join="", ponto_final=False, virgula=False)
                print("AS:", tipo_aorta.GetStringSelection())
                if tipo_aorta.GetStringSelection() == "coarse":
                    texto_label = self.text_label_plural(texto_label)

            if "#descrever_linha_porte_de_peso_sacro#" in texto_label:
                escolhas = ["central", "before", "after"]
                tipo_aorta = wx.SingleChoiceDialog(self, "Describe the position of the weight carrying line in relation to the sacrum.", "Weight carrying line", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_linha_porte_de_peso_sacro#", join="", ponto_final=False, virgula=False)

            if "#single_hd_inclinacao#" in texto_label:
                escolhas = ["", ", nonspecific to the method", ", of probable positional aspect"]

                tipo_aorta = wx.SingleChoiceDialog(self, "diagnostic hypothesis", "diagnostic hypothesis", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#single_hd_inclinacao#", join="", e=False)


            if "#complemento_vt#" in texto_label:
                escolhas = [
                    "",
                    "to be confirmed with full column radiographs.",
                ]

                tipo_aorta = wx.SingleChoiceDialog(self, "Complement the assessment of the transition vertebra?", "Complement the evaluation?", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label, "#complemento_vt#", join="")

            if "#descrever_tipo_opacidade#" in texto_label:
                escolhas = [
                    "",
                    "heterogeneous",
                    "reticulums",
                    "alveolar reticulum",
                    "interstitial",
                    "interstitial-alveolar",
                ]
                tipo_aorta = wx.SingleChoiceDialog(self,
                                                   "If you wish you can describe the opacity pattern found.",
                                                   "Opacity pattern", choices=escolhas)
                texto_label = self.fun_singleChoice_sem_e(tipo_aorta, escolhas, texto_label,
                                                          "#descrever_tipo_opacidade#", join="",
                                                          ponto_final=False, virgula=False)

            if "#desc_opa_pulmao_local#" in texto_label:
                escolhas = ["in the upper third", "in the middle third", "in the lower third", "in the perihilar region", "diffuse"]
                tipo_aorta = wx.MultiChoiceDialog(self, "what is the location " + self.label + " found in " + self.nome_anat + "?",
                                                  "Opacity description", choices=escolhas)
                modal_tipo = tipo_aorta.ShowModal()
                if modal_tipo == wx.ID_OK:
                    print(tipo_aorta.GetSelections())
                    aorta_tipo_select = tipo_aorta.GetSelections()
                    aorta_texto = ""
                    for item in aorta_tipo_select:
                        aorta_texto += escolhas[item]
                        aorta_texto += ", "
                    aorta_texto = aorta_texto[:-2]
                    aorta_texto = aorta_texto[::-1]
                    print(aorta_texto)
                    aorta_texto = aorta_texto.replace("oçret on ", "", 1)
                    aorta_texto = aorta_texto.replace(",", "dna ", 1)
                    aorta_texto = aorta_texto[::-1]
                    texto_label = texto_label.replace("#desc_opa_pulmao_local#", aorta_texto)
                    print(aorta_texto)
                    #if aorta_texto == ".":
                    #    texto_label = ""
                elif modal_tipo == wx.ID_CANCEL:
                    texto_label = ""

            if "#desc_opa_pulmao_hd#" in texto_label:
                escolhas = ["with air bronchograms",
                     "may correspond to an inflammatory / infectious process",
                     "being able to correspond to pneumonic process",
                     "to be correlated to clinical data",]
                tipo_aorta = wx.MultiChoiceDialog(self, "If you wish, here you can complement your description.",
                                                  "Description of the opacity", choices=escolhas)

                modal_tipo = tipo_aorta.ShowModal()
                if modal_tipo == wx.ID_OK:
                    print(tipo_aorta.GetSelections())
                    aorta_tipo_select = tipo_aorta.GetSelections()
                    aorta_texto = ""
                    for item in aorta_tipo_select:
                        aorta_texto += escolhas[item]
                        aorta_texto += ", "
                    aorta_texto = aorta_texto[:-2] + "."
                    aorta_texto = aorta_texto[::-1]
                    print(aorta_texto)
                    aorta_texto = aorta_texto[::-1]
                    print("Aqui:", aorta_texto)
                    texto_label = texto_label.replace("#desc_opa_pulmao_hd#", aorta_texto)
                    #if aorta_texto == ".":
                    #    texto_label = ""
                elif modal_tipo == wx.ID_CANCEL:
                    texto_label = ""

            if "#desc_partes_moles_hd#" in texto_label:
                escolhas = ["unspecific to the method", "may correspond to inflammatory edema",
                             "may be secondary to edema",
                             "being able to correspond to an inflammatory process",
                             "correlate to clinical data"]
                tipo_aorta = wx.MultiChoiceDialog(self, "Here you can complement your description.", "Description of the opacity",
                                                  choices=escolhas)
                modal_tipo = tipo_aorta.ShowModal()
                if modal_tipo == wx.ID_OK:
                    print(tipo_aorta.GetSelections())
                    aorta_tipo_select = tipo_aorta.GetSelections()
                    aorta_texto = ""
                    for item in aorta_tipo_select:
                        aorta_texto += escolhas[item]
                        aorta_texto += ", "
                    aorta_texto = aorta_texto[:-2] + "."
                    aorta_texto = aorta_texto[::-1]
                    print(aorta_texto)
                    aorta_texto = aorta_texto[::-1]
                    texto_label = texto_label.replace("#desc_partes_moles_hd#", aorta_texto)
                    print(aorta_texto)
                    #if aorta_texto == ".":
                    #    texto_label = ""
                elif modal_tipo == wx.ID_CANCEL:
                    texto_label = ""

            if "#desc_opa_sinus_hd#" in texto_label:
                escolhas = ["with mucosal thickening", "with formation of hydro level",
                             "may correspond to an acute inflammatory / infectious process",
                             "may correspond to an inflammatory / infectious process",
                             "being able to correspond to sinusitis",
                             "to be correlated to clinical data",
                             "to be correlated to clinical data",
                             ". Correlate with clinical data"]
                tipo_aorta = wx.MultiChoiceDialog(self, "Describe the type of aorta.", "Description of the aorta",
                                                  choices=escolhas)

                texto_label = self.fun_multiChoice_sem_e(tipo_aorta, escolhas, texto_label, "#desc_opa_sinus_hd#")

                texto_label = self.text_label_adequar_convencao(texto_label)


            if "#desc_opa_sinus_espesamento_mucoso_hd#" in texto_label:
                escolhas = ["with hydro level formation",
                             "may correspond to an acute inflammatory / infectious process",
                             "may correspond to an inflammatory / infectious process",
                             "being able to correspond to sinusitis",
                             "to be correlated to clinical data",
                             ". Correlate with clinical data"]
                tipo_aorta = wx.MultiChoiceDialog(self, "Describe", "Describe",
                                                  choices=escolhas)

                texto_label = self.fun_multiChoice_sem_e(tipo_aorta, escolhas, texto_label, "#desc_opa_sinus_espesamento_mucoso_hd#")
                texto_label = self.text_label_adequar_convencao(texto_label)



            if "#desc_corpo_estranho_hd#" in texto_label:
                escolhas = ["being able to correspond to free body",
                             "may correspond to calcification",
                             "being able to correspond to corticalized bone nucleus",
                             "being able to correspond to bone fragment",
                             "being able to correspond to a bone fragment due to fracture in the context of trauma",
                             "unspecific to the method.",
                             "which may correspond to a Baker's cyst with free calcified bodies",
                             "to be correlated to clinical data",
                             ". Correlate with clinical data",
                             ". Correlate with the correlate with the past medical history.",
                             ". Correlate with clinical data and patient correlate with the past medical history.",]
                tipo_aorta = wx.MultiChoiceDialog(self, "Describe", "Describe",
                                                  choices=escolhas)

                texto_label = self.fun_multiChoice_sem_e(tipo_aorta, escolhas, texto_label, "#desc_corpo_estranho_hd#")


            if "#descrever_correlacionar#" in texto_label:
                escolhas = [
                    "", ". Correlate with the correlate with the past medical history.", ". Correlate with clinical data.", ". Correlate with clinical data and patient correlate with the past medical history."
                ]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish, you can put the sentence to emphasize the importance of correlating with clinical data and patient history.", "correlate with clinical data", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_correlacionar#", join="", ponto_final=False, e=False, virgula=False)

            if "#descrever_listese_acentuacao#" in texto_label:
                escolhas = ["", "minimal", "small", "moderate", "sharp", "important"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish you can describe the accentuation of the retrolistese.", "Describe the degree of retrolistese.", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_listese_acentuacao#", join="", ponto_final=False, e=False, virgula=False)



            if "#descrever_tamanho#" in texto_label:
                escolhas = ["",
                     "small",
                     "diminutive",]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish you can describe the size.", "Describe the size.", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_tamanho#",join="", ponto_final=False, e=False, virgula=False)



            if "#descrever_grau_derrame_pleural_ex_pequeno_singular_masculino#" in texto_label:
                escolhas = ["",
                            "may correspond to pleural effusion",
                            "may correspond to a small pleural effusion",
                            "may correspond to moderate pleural effusion",
                            "may correspond to severe pleural effusion",
                            "may correspond to a major pleural effusion"
                            ]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish you can describe the degree of commitment of the finding", "Characterize the degree.", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_derrame_pleural_ex_pequeno_singular_masculino#", join=", ", ponto_final=False, e=False, virgula=False)


            if "#descrever_grau_derrame_pleural_bilateral_ex_pequeno_masculino#" in texto_label:
                escolhas = ["",
                             "which may correspond to bilateral pleural effusion",
                             "which may correspond to a small bilateral pleural effusion",
                             "which may correspond to moderate bilateral pleural effusion",
                             "being able to correspond to accentuated bilateral pleural effusion",
                             "may correspond to an important bilateral pleural effusion"]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish you can describe the degree of commitment of the finding", "Characterize the degree.", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_derrame_pleural_bilateral_ex_pequeno_masculino#", join=", ", ponto_final=False, e=False, virgula=False)

            if "#descrever_obliteracao_hd#" in texto_label:
                escolhas = ["",
                             "which may correspond to pleural effusion",
                             "being able to correspond to hemothorax",]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish you can describe the diagnostic hypothesis of pleural effusion", "diagnostic hypothesis", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_obliteracao_hd#", join=", ", ponto_final=False, e=False, virgula=False)


            if "#descrever_trageto_do_tubo#" in texto_label:
                escolhas = ["in an oblique path",
                            "in an oblique path lighting cranially",
                            "in a straight path",
                            ]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish you can describe the path of the tube.", "Tube path", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_trageto_do_tubo#", join="", ponto_final=False, e=False, virgula=False)


            if "#descrever_local_extremidade_do_tubo#" in texto_label:
                escolhas = [
                    "",
                    "with the distal end seen in the upper pulmonary third.",
                    "with distal end seen in the middle pulmonary third.",
                    "with the distal end seen in the lower pulmonary third.",
                    "with the distal end not seen.",
                ]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish you can describe the path of the tube.", "Tube path", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_local_extremidade_do_tubo#", join=", ", ponto_final=False, e=False, virgula=False)



            if "#descrever_grau_listese#" in texto_label:
                escolhas = ["grade I", "grade II", "grade III", "grade IV", "grade V"]
                tipo_aorta = wx.SingleChoiceDialog(self, "Define the degree of anterolysthesis.", "Anterolistesis", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label, "#descrever_grau_listese#", join="", ponto_final=False, e=False, virgula=False)


            if "#descrever_listese_hd#" in texto_label:
                escolhas = ["probably secondary to interapophyseal degeneration",
                             "with reduction of the anteroposterior diameter of the vertebral canal",
                             "probably secondary to degenerative changes in the elements of the posterior arches",
                             "compatible with isthmic lysis sequel."]

                tipo_aorta = wx.MultiChoiceDialog(self, "If you wish you can describe the diagnostic hypothesis from the list.", "Describe the degree of listing",
                                                  choices=escolhas)
                texto_label = self.fun_multiChoice_sem_e(tipo_aorta, escolhas, texto_label, "#descrever_listese_hd#")


            if "#num_fra_osteoporose#" in texto_label:
                self.num = wx.GetNumberFromUser("Percentage of vertebral body height reduction,\nuse a healthy vertebral body to calculate \nthe percentage in relation to the diseased vertebral body.", "", "Percentage of vertebral body height reduction", 0,
                                                0, 100, self)
                texto_label = texto_label.replace("#num_fra_osteoporose#", str(self.num))

            if "#num_parafuso_placa#" in texto_label:
                self.num = wx.GetNumberFromUser("What is the number of screws found?", "", "Number of screws", 0,
                                                0, 100, self)
                texto_label = texto_label.replace("#num_parafuso_placa#", str(self.num))


            if "#descrever_integridade_material_livre#" in texto_label:
                escolhas = [
                    "intact and without signs of release",
                     "intact and with no sign of release",
                     "intact and without signs of release",
                     "complete and with no sign of release",
                ]
                tipo_aorta = wx.SingleChoiceDialog(self, "If you wish, characterize the osteosynthesis.",
                                                   "Osteosynthesis", choices=escolhas)
                texto_label = self.fun_singleChoice(tipo_aorta, escolhas, texto_label,
                                                    "#descrever_integridade_material_livre#", join=", ",
                                                    ponto_final=False, e=False, virgula=False)


            if "#num_nodulo#" in texto_label:
                self.num = wx.GetNumberFromUser("How many nodules or nodule possibilities are visible?", "", "What is the number of nodules?", 0,
                                                0, 100, self)
                texto_label = texto_label.replace("#num_nodulo#", str(self.num))
                if self.num > 1:
                    texto_label = self.text_label_plural(texto_label)
                if self.num == 1:
                    texto_label = texto_label.replace("1", "one", 1)



            if "#num_Wib#" in texto_label:
                self.num = wx.GetNumberFromUser("Inform the angle of Wiberg", "", "Wiberg's angle", 0,
                                                0, 100, self)
                texto_label = texto_label.replace("#num_Wib#", str(self.num))
                if self.num > 39:
                    texto_label += " featuring acetabular hyper-coverage."
                else:
                    texto_label = texto_label.replace(",",".")

            if "#num_Wib_d#" in texto_label:
                self.num_d = wx.GetNumberFromUser("Enter Wiberg angle to the right", "", "Wiberg's angle", 0,
                                                0, 100, self)
                texto_label = texto_label.replace("#num_Wib_d#", str(self.num_d))

                self.num_e = wx.GetNumberFromUser("Enter the Wiberg angle on the left", "", "Wiberg's angle", 0,
                                                  0, 100, self)
                texto_label = texto_label.replace("#num_Wib_e#", str(self.num_e))

                if self.num_d > 39 and self.num_e > 39:
                    texto_label += " featuring bilateral acetabular hyper-coverage."
                elif self.num_d > 39:
                    texto_label += " featuring right acetabular hyper-coverage."
                elif self.num_e > 39:
                    texto_label += " characterizing acetabular hypercovering on the left."
                else:
                    texto_label = texto_label.replace(",", ".")

            if "#num_angulo_do_sulco_troclear#" in texto_label:
                self.num = wx.GetNumberFromUser("Inform the angle of the trochlear groove", "", "Trochlear groove angle", 0,
                                                0, 360, self)
                texto_label = texto_label.replace("#num_angulo_do_sulco_troclear#", str(self.num))
                if self.num > 145:
                    texto_label += " increased and may predispose to patellar instability."
                else:
                    texto_label += " within normal values."

            if "#num_Cobb#" in texto_label:
                self.num = wx.GetNumberFromUser("Inform the angle of Cobb", "", "Cobb angle", 0,
                                                0, 100, self)
                texto_label = texto_label.replace("#num_Cobb#", str(self.num))

                if self.num >= 10:
                    frase_escoliose = "Slight scoliotic deviation from the longitudinal axis of the spine "
                if self.num >= 20:
                    frase_escoliose = "Moderate scoliotic deviation of the longitudinal axis of the spine "
                if self.num >= 40:
                    frase_escoliose = "Severe scoliotic deviation of the longitudinal axis of the spine "
                if self.num == -1:
                    texto_label = ""

                frase_assimetria = "Asymmetry of the longitudinal axis of the column "
                if self.num >= 10:
                    texto_label = texto_label.replace(frase_assimetria, frase_escoliose)


            if "#num_halux_ex_valgo#" in texto_label:
                self.num = wx.GetNumberFromUser("Enter the hallux angle", "", "Hallux angle", 0,
                                                0, 360, self)

                if self.num >= 0:
                    frase_escoliose = "Hallux with angle of " + str(self.num) + " degrees, value within the normal range."
                if self.num >= 15:
                    frase_escoliose = "Hallux valgus light, with angle of " + str(self.num) + " degrees."
                if self.num >= 20:
                    frase_escoliose = "Moderate hallux valgus, with angle of " + str(self.num) + " degrees."
                if self.num >= 30:
                    frase_escoliose = "Severe hallux valgus, with angle of " + str(self.num) + " degrees."
                if self.num == -1:
                    texto_label = ""
                texto_label = texto_label.replace("#num_halux_ex_valgo#", frase_escoliose)



            if "#num_fer#" in texto_label:
                self.num = wx.GetNumberFromUser("Enter Ferguson angle", "", "Ferguson angle", 0,
                                                0, 100, self)
                texto_label = texto_label.replace("#num_fer#", str(self.num))
                if self.num < 35:
                    frase_lordose = " degrees."
                if self.num >= 35:
                    frase_lordose = " degrees."
                if self.num > 45:
                    frase_lordose = " degrees."
                texto_label += frase_lordose

            if "#num_als#" in texto_label:
                self.num = wx.GetNumberFromUser("Enter the lumbosacral angle\nRV = 130º-160º", "", "Lumbosacral angle",
                                                0, 0, 360, self)
                texto_label = texto_label.replace("#num_als#", str(self.num))

            if "#tipo_fra_og1#" in texto_label:
                escolhas = ["", "transverse", "oblique", "spiral", "longitudinal", "comminuted",
                             "impacted", "by avulsion", "on green branch"]
                tipo_fra = wx.GetSingleChoice("Type of fracture", "Fracture", escolhas)

                self.tipo_fra1 = tipo_fra

                escolhas = [ "", " without significant deviation", " without deviation", " with deviation", " with lateral deviation", " with medial deviation",
                             " with anterior deviation", " with posterior deviation", " with inferior deviation", " with superior deviation"]
                desvio_fra = wx.GetSingleChoice("Is there a deviation?", "Deviation", escolhas)

                escolhas = ["", " without joint extension", " with joint extension"]
                ex_art_fra = wx.GetSingleChoice("Does it have joint extension?", "Extension", escolhas)

                if desvio_fra != " " and ex_art_fra !="":
                    self.tipo_fra2 = desvio_fra + " and " + ex_art_fra
                elif desvio_fra != " " and ex_art_fra == "":
                    self.tipo_fra2 = desvio_fra[:-1] + ex_art_fra
                elif desvio_fra == " ":
                    self.tipo_fra2 = ex_art_fra

                texto_label = texto_label.replace("#tipo_fra_og1#", self.tipo_fra1)
                texto_label = texto_label.replace("#tipo_fra_og2#", self.tipo_fra2)

            if texto_label != "":
                texto_label = texto_label[::-1].replace(". ", ".", 1)

                # para evitar repetição da palavra espaço articular
                num_esp_art = texto_label.count(" oçapse od")
                if num_esp_art >= 2:
                    texto_label = texto_label.replace(" oçapse od", "", 1)
                print(texto_label)

                texto_label = texto_label[::-1]
                texto_label = texto_label.replace("  ", " ")
                texto_label = texto_label.strip()
                texto_label = texto_label[0].title() + texto_label[1:]
                texto_label += "\n"
                texto_label = texto_label.replace("  ", " ")
                texto_label = texto_label.replace("..", ".")
                texto_label = texto_label.replace(" ,", ",")
                texto_label = texto_label.replace(" .", ".")
                texto_label = texto_label.replace(",. ", ". ")
                texto_label = texto_label.replace(",.", ".")
                texto_label = texto_label.replace(".,", ",")

                # Nova correção
                texto_label = texto_label.replace("Redução do espaço articular da articulação", "Redução do espaço da articulação")
                texto_label = texto_label.replace("redução do espaço articular da articulação", "redução do espaço da articulação")
                texto_label = texto_label.replace("C8", "T1")

                if "mic_on" in texto_label:
                    self.fala_para_texto()
                    texto_label = texto_label.replace("mic_on", "")


                self.ultimo_texto_label = texto_label
                filename = "xrd80.ipn"
                with open(filename, "r") as file_object:
                    list_dics = json.load(file_object)
                    for dic in list_dics:
                        for key, value in dic.items():
                            print("TEXT LABEL:", texto_label)
                            print("Key:", key)
                            if texto_label == key +"\n":
                                print("texto_label == key:")
                                texto_label = value + "\n"

                self.panel_text.text_editor.WriteText(texto_label)

                # self.on_copiar_linha(texto_label.replace("\n", ""))
            try:
                texto_info = event_obj.GetHelpString(event_id).split("#info#")[1]
                self.panel_clinico.texto_info_clinica.SetValue(texto_info)
            except IndexError:
                print("Sem para info texto")
            try:
                imagem_info = wx.Image(event_obj.GetHelpString(event_id).split("#img#")[1]).ConvertToBitmap()
                self.panel_clinico.info_imagem.SetBitmap(imagem_info)
            except IndexError:
                print("Sem imagem para info te")
            try:
                texto_con = event_obj.GetHelpString(event_id).split("#con#")[1] + "\n\n"
                self.panel_clinico.conclusao_info_clinica.WriteText(texto_con)
            except IndexError:

                print("Without for completion")
            try:
                self.webpage = event_obj.GetHelpString(event_id).split("#webvideo#")[1]
                if self.webpage != None:
                    print("Com: webvideo " + self.webpage)
                    self.toolbar.EnableTool(self.id_do_youtube_tool, True)
                    self.toolbar.SetToolShortHelp(self.id_do_youtube_tool, "Video on the subject available !\n" + self.nome_anat.title()[0] + self.nome_anat[1:] + " " + self.label + ".")
            except IndexError:
                print("Sem: webvideo")
                self.toolbar.EnableTool(self.id_do_youtube_tool, False)
                self.toolbar.SetToolShortHelp(self.id_do_youtube_tool, "Watch a video about it on YouTube!\nWhen the icon gets active.")
                pass


class MyApp(wx.App):
    """Meu App"""
    # MaquinaLogin
    n = 2222

    # Plataforma
    plataforma = sys.platform
    print("Plataforma:", plataforma)

    # ID Autorizado
    mac_id = get_mac()
    print("Real Mac ID:", mac_id)
    mac_id = "105852886877588"
    #print("MEU PC ID UNICO:", mac_id)

    # PRODUTO DA COSMO
    app_id = "RX"

    #######################AAAAMMDDHHMMSS################
    tempo_expiracao_code = 90201205010203
    #####################################################

    real_time_int = 20140101010203

    # Time
    try:
        res = urlopen("http://just-the-time.appspot.com/")
        result = res.read().strip()
        result_str = result.decode("utf-8")
        real_time = result_str
        real_time_int = int(real_time.replace(" ", "").replace(":", "").replace("-", ""))

    except:
        result_str = "99999999999999,99999999999999,99999999999999"
        print("Sem Net")
        def OnInit(self):
            frame = wx.Frame(None)
            frame.Hide()
            msg_validada = wx.MessageBox(
                "Without internet access check your connection!",
                "No Internet access",
                parent=frame)
            frame.Destroy()
            return True

    criar_time = False

    filename = "xrd81.ipn"
    try:
        with open(filename, "r") as file_object:
            dic_t_maquina = json.load(file_object)

            criar_time = False
            for key, value in dic_t_maquina.items():
                time_primeira_inst = key
                time_vencimento_inst = value

                time_vencimento_inst_str = str(time_vencimento_inst)
                time_primeira_inst_str = str(time_primeira_inst)

                if key == "201712345678901234567890":
                    print("Criar ID para Maquina")
                    criar_time = True

                    # Criar ID
            if criar_time == True:
                with open(filename, "w") as file_object:
                    id_antigo = dic_t_maquina
                    for key, value in id_antigo.items():
                        real_time = real_time.replace(" ", "").replace(":", "").replace("-", "")

                        key_id_atual = real_time + ":" + app_id + str(mac_id)
                        dic_t_maquina_novo = {}

                        # - # - # - # - # - # - NÃO USAR MAIS # - # - # - # - # - # - #
                        dic_t_maquina_novo[key_id_atual] = 20150924010203
                        # - # - # - # - # - # - # - # - # - # - # - # - #

                        json.dump(dic_t_maquina_novo, file_object)

                tempo_comparar_atual = result_str.replace(" ", "").replace(":", "").replace("-", "")
                tempo_comparar_atual = int(tempo_comparar_atual)

                tempo_comparar_vencimento = time_vencimento_inst_str.replace(" ", "").replace(":", "").replace("-", "")
                tempo_comparar_vencimento = int(tempo_comparar_vencimento)


            elif criar_time == False and result_str != "99999999999999,99999999999999,99999999999999":
                print("Time Atual: " + result_str)
                print("Time Prime:", time_primeira_inst)
                print("Time Vencimento:", time_vencimento_inst)

                tempo_comparar_atual = result_str.replace(" ", "").replace(":", "").replace("-", "")
                tempo_comparar_atual = int(tempo_comparar_atual)

                tempo_comparar_vencimento = time_vencimento_inst_str.replace(" ", "").replace(":", "").replace("-", "")
                tempo_comparar_vencimento = int(tempo_comparar_vencimento)

                if tempo_comparar_vencimento < tempo_comparar_atual:
                    print("ID time expired!")

                    def OnInit(self):
                        frame = wx.Frame(None)
                        frame.Hide()
                        print("Essa ID vencida. 1")
                        msg_validada = wx.MessageBox("ID expired! Contact Cosmo Radiology at WhatsApp (41)98444-9186 for a quick reply! https://www.peteralexandercharles.com/",
                                                     "ID expired",
                                                     parent=frame)

                        msg_deseja_validar = wx.MessageDialog(frame,"Would you like to validate an ID already purchased ?",
                                                           "Validar ID",
                                                           style=wx.YES_NO|wx.ICON_INFORMATION)

                        modal_validar = msg_deseja_validar.ShowModal()
                        if modal_validar == wx.ID_YES:
                            print("Let's validate your ID!")
                            frame_validar = MyFrame_Key(frame, destroi_parent=True)

                        elif modal_validar == wx.ID_NO:
                            print("Res: You do not wish to validate.")
                            frame.Destroy()
                        return True


                elif 2 != 2:

                    print("ID já em uso!")
                    def OnInit(self):
                        frame = wx.Frame(None)
                        frame.Hide()
                        msg_validada = wx.MessageBox("Contact Cosmo Radiology at WhatsApp (41)98444-9186 for a quick reference! We've quickly released a free ID for you to try out our Assistant! https://www.peteralexandercharles.com/",
                                                     "ID already in use",
                                                     parent=frame)

                        msg_deseja_validar = wx.MessageDialog(frame,"Would you like to validate your ID ?",
                                                           "Validar ID",
                                                           style=wx.YES_NO|wx.ICON_INFORMATION)

                        modal_validar = msg_deseja_validar.ShowModal()
                        if modal_validar == wx.ID_YES:
                            print("Let's validate your ID!")
                            frame_validar = MyFrame_Key(frame, destroi_parent=True)

                        elif modal_validar == wx.ID_NO:
                            print("Res: Não deseja validar.")
                            frame.Destroy()
                        return True

        try:
            if n == 2222 and tempo_comparar_vencimento >= tempo_comparar_atual and time_primeira_inst.split(":")[1] == app_id + str(mac_id)\
                    and tempo_expiracao_code > real_time_int:
            #if n == 2222 and tempo_comparar_vencimento >= tempo_comparar_atual and 2 == 2:
                print("Entrada Autorizada.")

                def OnInit(self):
                    """For MainLoop."""
                    self.frame_logo = MyFrame_Apresentacao(None, style=wx.STAY_ON_TOP|wx.CAPTION, link=False)
                    self.frame = MyFrame(None, "X-Ray Assistente - Cosmo Radiology - v 2.1.4")
                    self.timer = wx.Timer(self)
                    self.Bind(wx.EVT_TIMER, self.on_update_time, self.timer)
                    self.timer.Start(2500)
                    return True

                def on_update_time(self, event):
                    """Tempo"""
                    print("Show Main Frame!!!")
                    self.frame.Show()
                    self.frame_logo.Close()
                    self.timer.Stop()
                    self.timer.Destroy()



            elif tempo_expiracao_code < real_time_int:
                print("Unauthorized entry.")
                def OnInit(self):
                    frame = wx.Frame(None)
                    frame.Hide()
                    print("Essa ID vencida. 2")
                    msg_validada = wx.MessageBox(
                        "Contact Cosmo Radiology at WhatsApp (41)98444-9186 for a quick reply! We quickly released a free license for you to test our Assistant! https://www.peteralexandercharles.com/",
                        "Unauthorized entry.",
                        parent=frame)
                    frame.Destroy()
                    return True

        except IndexError:
            print("IndexError")
            def OnInit(self):
                frame = wx.Frame(None)
                frame.Hide()
                msg_validada = wx.MessageBox("Welcome! X-Ray Assistant ID Validated! Chess customer if you need to contact us at WhatsApp (41) 98444-9186 for a quick reply! https://www.peteralexandercharles.com/",
                                             "Validated ID",
                              parent=frame)
                msg_firewall = wx.MessageBox(
                    "Important message for you! Your Assistant needs you to enable it again and click on Allow in Windows Defender Firewall to enable necessary updates in your Assistant!",
                    "Attention!", style=wx.ICON_INFORMATION, parent=frame)

                frame.Destroy()
                return True

        except NameError:
            print("Sem Net:!")


    except FileNotFoundError:

            filename = "xrd81.ipn"

            with open(filename, "w") as fileobject:

                real_time = real_time.replace(" ", "").replace(":", "").replace("-", "")
                key_id_atual = real_time + ":" + app_id + str(mac_id)
                key_id_atual = key_id_atual.replace(" ", "").replace("-", "")
                idmaq = {}
                ######################AAAAMMDD#HHMMSS####################
                idmaq[key_id_atual] = 20201215010203
                ####################################
                json.dump(idmaq, fileobject)
                print("Criado: " + filename)

            def OnInit(self):
                frame = wx.Frame(None)
                frame.Hide()
                msg_validada = wx.MessageBox(
                    "Welcome! X-Ray Assistant ID Validated! Chess customer if you need to contact us at WhatsApp (41) 98444-9186 for a quick reply! https://www.peteralexandercharles.com/",
                    "ID validado",
                    parent=frame)
                msg_firewall = wx.MessageBox(
                    "Important message for you! Your Assistant needs to enable it in the Firewall again and click enable in Windows Defender Firewall to enable necessary updates in your Assistant!",
                    "Attention!", style=wx.ICON_INFORMATION, parent=frame)

                frame.Destroy()
                return True

    except IndexError:
        def OnInit(self):
            frame = wx.Frame(None)
            frame.Hide()
            msg_validada = wx.MessageBox(
                "Welcome! X-Ray Assistant ID Validated! Chess customer if you need to contact us at WhatsApp (41) 98444-9186 for a quick reply! https://www.peteralexandercharles.com/",
                "ID validada",
                parent=frame)
            msg_firewall = wx.MessageBox(
                "Important message for you! Your Assistant needs to enable it in the Firewall again and click enable in Windows Defender Firewall to enable necessary updates in your Assistant!",
                "Attention!", style=wx.ICON_INFORMATION, parent=frame)

            frame.Destroy()
            return True

    except json.decoder.JSONDecodeError:
        def OnInit(self):
            frame = wx.Frame(None)
            frame.Hide()
            msg = wx.MessageBox(
                "JSONDecodeError\n\nContate a Cosmo Radiology pelo WhatsApp (41)98444-9186 para atendimento!\n\nSite: https://www.peteralexandercharles.com/\n\nCÓDIGO DO ERRO:155",
                "JSONDecodeError.", parent=frame)
            frame.Destroy()
            return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()


