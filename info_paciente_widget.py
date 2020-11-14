#!/usr/bin/env python
# -*- coding: windows-1252 -*-

"""Class to collect patient information and which
 exams you want to do the report."""

import wx
import wx.lib.platebtn as platebtn


class InfoPaciente():
    """Colour widgetes to collect patient information.
    and exams want to make the report."""
    def __init__(self):
        """Initialize class attributes."""

    def tecnica_widget(self):
        bitmap = wx.Bitmap("xrd128.ipn", wx.BITMAP_TYPE_PNG)
        self.platebtn_tecnica = platebtn.PlateButton(self,
label="What exam do you want to do the report?")
        self.platebtn_tecnica.SetBitmap(bitmap)
        self.menu_tecnica = wx.Menu("Select:")
        self.menu_item_torax = self.menu_tecnica.Append(-1, "Thorax")
        self.menu_item_coluna_lombar = self.menu_tecnica.Append(-1, "Lomar Spine", "222222")
        self.platebtn_tecnica.SetMenu(self.menu_tecnica)

        return self.platebtn_tecnica



class MyPanel_info(wx.Panel):
    """Panel to get patient information
     and select the exam."""
    def __init__(self, parent):
        """Initialize class attributes."""
        super(MyPanel_info, self).__init__(parent)

        # Layout Manager 1
        down = wx.BoxSizer(wx.VERTICAL)
        row1 = wx.BoxSizer()

        # Widgets

        # Widget Label | Patient's name
        nome = wx.StaticText(self, label="Patient:")
        row1.Add(nome, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        # Widget Patient's name
        self.nome_paciente_text_ctrl = wx.TextCtrl(self)
        row1.Add(self.nome_paciente_text_ctrl, 1, wx.EXPAND|wx.ALL, 5)

        # Clear patient name from text box
        clear_img = wx.Image("xrd129.ipn").ConvertToBitmap()
        self.button_clear = platebtn.PlateButton(self, -1, "")
        self.button_clear.SetBitmap(clear_img)
        self.button_clear.SetToolTip("Clear patient name from text box")
        row1.Add(self.button_clear, 0, wx.RIGHT, 5)

        # Down 1 line
        down.Add(row1, 0, wx.EXPAND)

        # Row 2
        row2 = wx.BoxSizer()

        # Widget
        bitmap = wx.Bitmap("xrd128.ipn", wx.BITMAP_TYPE_PNG)
        self.platebtn_tecnica = platebtn.PlateButton(self,
                                                     label="Which report do you want to do?")
        self.platebtn_tecnica.SetBitmap(bitmap)
        self.platebtn_tecnica.SetToolTip("Templetes standards")
        self.menu_tecnica = wx.Menu("Select default template:")

        # Head
        menu_cabeca = wx.Menu()
        self.menu_item_cranio = menu_cabeca.Append(-1, "Skull")
        self.menu_item_seios_da_face = menu_cabeca.Append(-1, "Sinuses")
        self.menu_item_cavum = menu_cabeca.Append(-1, "Cavum")
        self.menu_item_ossos_da_face = menu_cabeca.Append(-1, "Skull Bones")
        self.menu_item_ossos_nasais = menu_cabeca.Append(-1, "Nasal bones")
        self.menu_item_mandibula = menu_cabeca.Append(-1, "Jaw")
        self.menu_item_atm = menu_cabeca.Append(-1, "Temporomandibular joints")
        self.menu_tecnica.Append(-1, "Head", menu_cabeca)

        # Spine
        menu_coluna = wx.Menu()
        self.menu_item_coluna_cervical = menu_coluna.Append(-1, "Cervical")
        self.menu_item_coluna_toracica = menu_coluna.Append(-1, "Thoracic")
        self.menu_item_coluna_toraco_lombar = menu_coluna.Append(-1, "Thoracic and lombar")
        self.menu_item_coluna_lombar = menu_coluna.Append(-1, "Lombar")
        self.menu_item_coluna_lombossacra = menu_coluna.Append(-1, "Lumbar and sacral")
        self.menu_item_coluna_sacro_coccigea = menu_coluna.Append(-1, "Sacrum and coccyx")
        self.menu_item_coluna_total = menu_coluna.Append(-1, "Full spine")
        self.menu_tecnica.Append(-1, "Spine", menu_coluna)

        # Thorax
        torax_menu = wx.Menu()
        self.menu_item_torax = torax_menu.Append(-1, "Thorax")
        self.menu_item_arcos_costais_a_direita = torax_menu.Append(-1, "Coastal arches on right")
        self.menu_item_arcos_costais_a_esquerda = torax_menu.Append(-1, "Coastal arches on the left")
        self.menu_tecnica.Append(-1, "Thorax", torax_menu)

        # Abdomen
        menu_abdomen = wx.Menu()
        self.menu_item_abdomen_simples = menu_abdomen.Append(-1, "Simple abdomen")
        self.menu_item_abdome_agudo_simples = menu_abdomen.Append(-1, "Simple acute abdomen")
        self.menu_tecnica.Append(-1, "Abdomen", menu_abdomen)

        # Joints
        self.menu_item_articulacoes = self.menu_tecnica.Append(-1, "Joints")

        # Shoulder | Clavicle | Scapula
        menu_oce = wx.Menu()
        self.menu_item_ombro_direito = menu_oce.Append(-1, "Right shoulder")
        self.menu_item_ombro_esquerdo = menu_oce.Append(-1, "Left shoulder")
        self.menu_item_clavicula_direita = menu_oce.Append(-1, "Right clavicle")
        self.menu_item_clavicula_esquerda = menu_oce.Append(-1, "Left clavicle")
        self.menu_item_escapula_direita = menu_oce.Append(-1, "Right scapula")
        self.menu_item_escapula_esquerda = menu_oce.Append(-1, "Left scapulaa")
        self.menu_tecnica.Append(-1, "Shoulder | Clavicle | Scapula", menu_oce)

        # Upper limb
        menu_membro_superior = wx.Menu()
        self.menu_item_braco_direito = menu_membro_superior.Append(-1, "Right arm")
        self.menu_item_braco_esquerdo = menu_membro_superior.Append(-1, "Left arm")
        self.menu_item_cotovelo_direito = menu_membro_superior.Append(-1, "Right Elbow")
        self.menu_item_cotovelo_esquerdo = menu_membro_superior.Append(-1, "Left Elbow")
        self.menu_item_antebraco_direito = menu_membro_superior.Append(-1, "Right Forearm")
        self.menu_item_antebraco_esquerdo = menu_membro_superior.Append(-1, "Left Forearm")
        self.menu_item_punho_direito = menu_membro_superior.Append(-1, "Right Wrist")
        self.menu_item_punho_esquerdo = menu_membro_superior.Append(-1, "Left Wrist")
        self.menu_item_dedos_da_mao_direita = menu_membro_superior.Append(-1, "Right hand fingers")
        self.menu_item_dedos_da_mao_esquerda = menu_membro_superior.Append(-1, "Left hand fingers")
        self.menu_item_mao_direita = menu_membro_superior.Append(-1, "Right hand")
        self.menu_item_mao_esquerda = menu_membro_superior.Append(-1, "Left hand")
        self.menu_tecnica.Append(-1, "Upper limb", menu_membro_superior)


        # Bacia | Quadril | Fêmur | Coxa
        menu_bacia_quadril_femur = wx.Menu()
        self.menu_item_bacia = menu_bacia_quadril_femur.Append(-1, "Pelvic")
        self.menu_item_quadril_direito = menu_bacia_quadril_femur.Append(-1, "Right hip")
        self.menu_item_quadril_esquerdo = menu_bacia_quadril_femur.Append(-1, "Left hip")
        self.menu_item_femur_direito = menu_bacia_quadril_femur.Append(-1, "Right femur")
        self.menu_item_femur_esquerdo = menu_bacia_quadril_femur.Append(-1, "Left femur")
        self.menu_item_coxa_direita = menu_bacia_quadril_femur.Append(-1, "Right thigh and femur")
        self.menu_item_coxa_esquerda = menu_bacia_quadril_femur.Append(-1, "Left thigh and femur")
        self.menu_tecnica.Append(-1, "Pelvic | Femur | Thigh", menu_bacia_quadril_femur)


        # Joelho | Perna | Tornozelo | Pé
        menu_joelho_perna_tornozelo = wx.Menu()

        # Right knee
        menu_joelho_direito = wx.Menu("Right knee\tMenu")
        menu_joelho_perna_tornozelo.Append(-1, menu_joelho_direito.GetTitle(), menu_joelho_direito)
        self.menu_item_joelho_direito = menu_joelho_direito.Append(-1, "Right knee")
        menu_joelho_direito.AppendSeparator()
        self.menu_item_joelho_direito_com_carga = menu_joelho_direito.Append(-1, "Right knee with load")
        menu_joelho_direito.AppendSeparator()
        self.menu_item_joelho_direito_com_axial_de_patela = menu_joelho_direito.Append(-1, "Right knee with axial patella")


        menu_joelho_esquerdo = wx.Menu("Left knee\tMenu")
        menu_joelho_perna_tornozelo.Append(-1, menu_joelho_esquerdo.GetTitle(), menu_joelho_esquerdo)
        self.menu_item_joelho_esquerdo = menu_joelho_esquerdo.Append(-1, "Left knee")
        menu_joelho_esquerdo.AppendSeparator()
        self.menu_item_joelho_esquerdo_com_carga = menu_joelho_esquerdo.Append(-1, "Left knee with load")
        menu_joelho_esquerdo.AppendSeparator()
        self.menu_item_joelho_esquerdo_com_axial_de_patela = menu_joelho_esquerdo.Append(-1, "Left knee with axial patella")


        # Knee | Leg | Ankle | Foot
        self.menu_item_perna_direita = menu_joelho_perna_tornozelo.Append(-1, "Right leg")
        self.menu_item_perna_esquerda = menu_joelho_perna_tornozelo.Append(-1, "Left leg")
        self.menu_item_tornozelo_direito = menu_joelho_perna_tornozelo.Append(-1, "Right ankle")
        self.menu_item_tornozelo_esquerdo = menu_joelho_perna_tornozelo.Append(-1, "Left ankle")
        self.menu_item_pe_direito = menu_joelho_perna_tornozelo.Append(-1, "Right foot")
        self.menu_item_pe_esquerdo = menu_joelho_perna_tornozelo.Append(-1, "Left foot")
        self.menu_item_calcaneo_direito = menu_joelho_perna_tornozelo.Append(-1, "Right calcaneus")
        self.menu_item_calcaneo_esquerdo = menu_joelho_perna_tornozelo.Append(-1, "Left calcaneus")
        self.menu_tecnica.Append(-1, "Knee | Leg | Ankle | Foot", menu_joelho_perna_tornozelo)

        # Contrasted
        menu_contrastados = wx.Menu()
        self.menu_item_urografia_excretora = menu_contrastados.Append(-1, "Excretory urography")
        self.menu_item_transito_intestinal = menu_contrastados.Append(-1, "Intestinal transit")
        self.menu_item_esofago_estomago_e_duodeno_contrastado = menu_contrastados.Append(-1, "Esophagus Stomach and Contrast Duodenum")
        self.menu_item_enema_opaco = menu_contrastados.Append(-1, "Opaque Enema")
        self.menu_item_dacriocistografia = menu_contrastados.Append(-1, "Dacryocystography")
        self.menu_item_uretrocistografia_miccional = menu_contrastados.Append(-1, "Urinary urethrocystography")
        self.menu_item_uretrocistografia_retrograda = menu_contrastados.Append(-1, "Retrograde urethrocystography")
        self.menu_item_uretrocistografia_retrograda_e_miccional = menu_contrastados.Append(-1, "Retrograde and voiding urethrocystography")
        self.menu_item_histerossalpingografia = menu_contrastados.Append(-1, "Hysterosalpingography")
        self.menu_tecnica.Append(-1, "Contrasted", menu_contrastados)

        # Specials
        menu_especiais = wx.Menu()
        self.menu_item_mao_para_idade_ossea_masc = menu_especiais.Append(-1, "Bone Age Hand | Male")
        self.menu_item_mao_para_idade_ossea_fem = menu_especiais.Append(-1, "Bone Age Hand | Female")
        self.menu_item_escanometria = menu_especiais.Append(-1, "Scanometry")
        self.menu_item_legg_calve_perthes_pelve = menu_especiais.Append(-1, "Legg Calve perthes pelvis")
        self.menu_tecnica.Append(-1, "Specials", menu_especiais)
        self.platebtn_tecnica.SetMenu(self.menu_tecnica)
        row2.Add(self.platebtn_tecnica, 1, wx.ALL, 5)

        # Apagar texto do editor
        bitmap = wx.Image("xrd127.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.apagar_texto = platebtn.PlateButton(self, -1)
        self.apagar_texto.SetToolTip("""Clear text editor,
if it's already empty!
return with text
previous..""")
        self.apagar_texto.SetBitmap(bitmap)
        row2.Add(self.apagar_texto, 0, wx.ALL, 5)


        down.Add(row2, 0, wx.EXPAND)

        # SetSizer
        self.SetSizer(down)

        # Nome paciente variavel
        self.nome_paciente = ""


        # Bind
        self.nome_paciente_text_ctrl.Bind(wx.EVT_TEXT, self.on_get_paciente_name)
        self.Bind(wx.EVT_MENU, self.on_click_menu_item, self.menu_item_torax)
        self.Bind(wx.EVT_BUTTON, self.on_pop_menu, self.platebtn_tecnica)


    def on_get_paciente_name(self, event):
        """Capture the patient's name and store it in a variable."""
        self.nome_paciente = self.nome_paciente_text_ctrl.GetValue().title().strip()
        print(self.nome_paciente)
        event.Skip()

    def on_pop_menu(self, event):
        """Function to open the platebutton menu"""
        self.platebtn_tecnica.PopupMenu(self.menu_tecnica)


    def on_click_menu_item(self, event):
        """When selecting which rx to make the report shows standard template"""
        event_title = event.EventObject
        print("Return chest template!")
        event.Skip()