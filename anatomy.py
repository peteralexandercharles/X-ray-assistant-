#!/usr/bin/env python
#-*- coding: windows-1252 -*-

import wx
import wx.lib.platebtn as platebtn
import json

class Anatomy():
    """Initialize class attributes."""
    def __init__(self):
        """Initialize class attributes."""

    def heart(self, x, y, largura, altura):
        """Return custom button. Must define
        the position by x and y."""
        # heart
        style_plt = platebtn.PB_STYLE_NOBG
        #style_plt = platebtn.PB_STYLE_SQUARE
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip("Heart")
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)

        self.menu_coracao = wx.Menu("Heart")
        menu = wx.Menu("cardiothoracic ratio")
        menu.Append(-1, "normal", "#r#cardiothoracic ratio is normal.#r#"
                                  "#info#The cardiothoracic ratio is a radiological examination for approximate evaluation of increased cardiac silhouette. It is the ratio between the maximum transversal cardiac diameter and the diameter of the rib cage in deep inspiration. It usually corresponds to 0.5 in adults, and should be less than 0.65 in newborns and less than 0.55 in infants (values above this configure cardiomegaly.\nit is only valid in normolithic individuals.\n in brevilinear patients or in obesity, the increase of the diaphragm causes a 'lying heart' cardiac horizontalization, with false enlargement of the cardiac silhouette because what is measured in this case is no longer the transverse diameter of the heart but an intermediate diameter between the transverse and longitudinal. \In short or obese patients, the enlargement of the diaphragm causes a horizontal 'lying heart', with a false enlargement of the cardiac silhouette because what is measured in this case is no longer the transverse diameter of the heart but an intermediate diameter between the transverse and the longitudinal. \In pulmonary pathologies as well as in spine pathologies, with anatomical deviations of the interrelation of the thoracic organs, this index can be altered without cardiac cause.[1]\nBraunwald, Treaty of Cardiology 8e. Spanish edition, Elsevier, 2009 ISBN-13: 978-8480863766#info#"
                                  "#bloquear_img#screenshot-www.google.com.br-2018.08.14-12-20-03.png#bloquear_img#"
                                  "#webvideo#https://youtu.be/lrxBeKouTWo#webvideo#")
        menu.AppendSeparator()

        menu.Append(-1, "discreetly increased", "#r#cardiothoracic ratio at the upper limit of normality.#r#"
                                                   "#info#Especially in patients who have had recent cardiac surgery, an increase in the cardiac figure may indicate pericardial bleeding. Here another patient who had valve replacement. Observe the size of the large heart. There is redistribution of the pulmonary vessels, which indicates heart failure. The CT image shows a large pericardial effusion. Always compare these postoperative chest films with the preoperative ones.#info#"
                                                   "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-19-47-52.png#bloquear_img#"
                                                   "#con#Discrete increase in cardiothoracic ratio.#con#"
                                                   "#webvideo#https://youtu.be/oG_bE2x5LG8#webvideo#")

        menu.Append(-1, "increased", "#r#increased cardiothoracic ratio.#r#"
                                     "#info#Pericardial effusion: Whenever we come across a large figure of the heart, we should always be aware of the possibility of pericardial effusion simulating a large heart. In the chest radiography, it seems that this patient has the heart dilated, while at CT it is clear that it is the pericardial effusion that is responsible for the increased cardiac figure. Especially in patients who have had recent cardiac surgery, an increased cardiac figure may indicate pericardial bleeding.#info#"
                                     "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-19-37-19.png#bloquear_img#"
                                     "#con#Increase of cardiothoracic ratio.#con#"
                                     "#webvideo#https://youtu.be/hhERi64kU3o#webvideo#")

        menu.Append(-1, "increased | AP", "#r#Even with radiography having been performed in PA and dorsal decubitus there are signs of cardiomegaly.#r#"
                                          "#info#Relevant measurements in patient with heart failure.#info#"
                                          "#bloquear_img#screenshot-radiopraxis.com-2018.08.14-19-41-24.png#bloquear_img#"
                                          "#webvideo#https://youtu.be/EWBgmdbmI-Q#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "impaired evaluation", "#r#cardiothoracic ratio with impaired evaluation.#r#"
                                                 "#webvideo#https://youtu.be/lrxBeKouTWo#webvideo#")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        self.menu_coracao.AppendSeparator()


        # acimaOK1

        menu = wx.Menu("Silhueta cardíaca")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "normal", "#r#Cardiac silhouette within normal parameters.#r#"
                                  "#webvideo#https://youtu.be/TyZmRjjODIc#webvideo#")
        menu.AppendSeparator()

        menu.Append(-1, "partial loss", "#r#Partial loss of cardiac silhouette.#r#"
                                             "#info#Silhouette Sign This is a very important sign. It allows us to find subtle pathologies and locate them in the chest.  The loss of the normal silhouette of a structure is called the sign of the silhouette. Here is an example to explain the sign of the silhouette: The heart is previously located in the chest and is delimited by the tongue of the left lung.  The difference in density between the heart and the air in the lung allows us to see the silhouette of the left ventricle.  When there is something in the lingula with the same 'density of water' as the heart, the normal silhouette will be lost (blue arrow). When there is pneumonia in the lower left lobe, which is located more later in the chest, the left ventricle will still be limited by air in the lingula and we will still see the silhouette of the heart (red arrow).#info#"
                                             "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-17-19-11.png#bloquear_img#"
                                             "#con#Sign of loss of left ventricle silhouette.#con#"
                                         "#webvideo#https://youtu.be/q8uG-9FWfbM#webvideo#")

        menu.Append(-1, "partial loss on the right", "#r#Partial loss of heart silhouette on the right.#r#"
                                             "#info#Silhouette Sign This is a very important sign. It allows us to find subtle pathologies and locate them in the chest.  The loss of the normal silhouette of a structure is called the sign of the silhouette. Here is an example to explain the sign of the silhouette: The heart is previously located in the chest and is delimited by the tongue of the left lung.  The difference in density between the heart and the air in the lung allows us to see the silhouette of the left ventricle.  When there is something in the lingula with the same 'density of water' as the heart, the normal silhouette will be lost (blue arrow). When there is pneumonia in the lower left lobe, which is located more later in the chest, the left ventricle will still be limited by air in the lingula and we will still see the silhouette of the heart (red arrow).#info#"
                                             "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-17-19-11.png#bloquear_img#"
                                             "#con#Sign of loss of left ventricle silhouette.#con#"
                                                   "#webvideo#https://youtu.be/R5_4KPZGiJE#webvideo#")

        menu.Append(-1, "partial loss on the left", "#r#Partial loss of heart silhouette on the left.#r#"
                                             "#info#Silhouette Sign This is a very important sign. It allows us to find subtle pathologies and locate them in the chest.  The loss of the normal silhouette of a structure is called the sign of the silhouette. Here is an example to explain the sign of the silhouette: The heart is previously located in the chest and is delimited by the tongue of the left lung.  The difference in density between the heart and the air in the lung allows us to see the silhouette of the left ventricle.  When there is something in the lingula with the same 'density of water' as the heart, the normal silhouette will be lost (blue arrow). When there is pneumonia in the lower left lobe, which is located more later in the chest, the left ventricle will still be limited by air in the lingula and we will still see the silhouette of the heart (red arrow).#info#"
                                             "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-17-19-11.png#bloquear_img#"
                                             "#con#Sign of loss of left ventricle silhouette.#con#"
                                                    "#webvideo#https://youtu.be/qVXNjrKYf70#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "impaired evaluation", "#r#Cardiac silhouette with impaired evaluation.#r#"
                                                 "#webvideo#https://youtu.be/bU0Nm7JFJtU#webvideo#")

        # EN youtube videos yet here.

        self.menu_coracao.AppendSeparator()
        menu_fisio = wx.Menu("Physiological findings")
        self.menu_coracao.Append(-1, menu_fisio.GetTitle(), menu_fisio)
        menu_fisio.Append(-1, "Epicardial fat pads", "#r#Mass or nebular opacity at the costodiaphragmatic angle (direct/left/bilateral) with generally visible cardiac and diaphragmatic silhouettes, typical epicardial fat pad finding.#r#"
                                         "#info#Epicardial fat cushions Dr. Ayush Goel and Dr. Henry Knipe et al. are normal structures that are at the cardiophrenic angle, more to the right. Not surprisingly, they are more prominent in obese patients. Pathology They may be affected by fat necrosis (see: epipericardial fat necrosis).  Radiographic features Simple opaque or nebular radiography at the costodiaphragmatic angle Cardiac and generally visible CT silhouettes easily differentiate the epicardial fat from a different pathology than a lipoma Differential diagnosis Sometimes they are large enough to simulate pathology and can be confused with: lipoma or other pericardial cyst tumor (especially on the right) Morgagni's hernia epicardial lymphadenopathy pleural tumor#info#"
                                         "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-21-16-47.png#bloquear_img#"
                                         "#con#The radiographic analysis showed a typical image of an epicardial fat pad found without pathological connotation.#con#"
                                         "#webvideo#https://youtu.be/AFZtL9OCiIs#webvideo#")

        menu_pat = wx.Menu("Pathological findings")
        self.menu_coracao.Append(-1, menu_pat.GetTitle(), menu_pat)

        menu_pat.Append(-1, "Cardiac failure", "#r#enlargement of the heart, prominent central vessels, presence of Kerley's B lines, sparse lung opacifications (interstitial infiltrates), cranial reversal of the circulation (prominent upper vessels), and may infer some degree of heart failure. Correlate with clinical examination findings.#r#"
                                                               "#info#Insuficiência Cardíaca: Dr. Yuranga Weerakkody e o Dr. Jeremy Jones et al. Este é um artigo básico para estudantes de medicina e outros não radiologistas A insuficiência cardíaca é uma síndrome de disfunção ventricular cardíaca, em que o coração é incapaz de bombear o suficiente para atender às necessidades de fluxo sanguíneo do corpo. Apresentação clínica Embora seja útil dividir os sinais e sintomas de insuficiência cardíaca de acordo com o grau de disfunção ventricular esquerda ou direita, o coração é uma bomba integrada e o paciente geralmente se apresenta com ambos os conjuntos de sinais e sintomas. Além disso, sinais e sintomas podem refletir causas específicas ou agravantes da insuficiência cardíaca. Insuficiência ventricular esquerda Os pacientes geralmente relatam fadiga, dispneia aos esforços e, em casos graves, em repouso. A ortopneia, a dispneia paroxística noturna e a respiração de Cheyne-Stokes também podem ser uma característica. No exame, pode-se observar taquipneia, dispneia, taquicardia, hipotensão e cianose. A palpação pode revelar uma batida apical lateralmente deslocada, enquanto a ausculta cardíaca pode provocar sopros, como estenose aórtica ou regurgitação mitral. Características de edema pulmonar, como estertores bibasais inspiratórios não clareados ao tossir, sons respiratórios diminuídos e embotamento à percussão também podem ser notados. Insuficiência ventricular direita Os sintomas incluem inchaço do tornozelo, fadiga, inchaço abdominal / desconforto e noctúria. Evidências de insuficiência ventricular direita podem se manifestar como edema periférico (se for grave até as coxas e sacro), ascite, hepatomegalia e pressão venosa jugular elevada (JVP). A JVP pode ser ainda mais acentuada pelo refluxo hepatojugular. Sopros cardíacos também podem ser ouvidos, geralmente regurgitação tricúspide. A gravidade clínica varia significativamente e geralmente é classificada de acordo com a New York Heart Association, que é graduada de acordo com a quantidade de atividade física diminuída. Patologia Danos no miocárdio devido a infartos do miocárdio, cardiomiopatia e miocardite podem causar ou agravar a insuficiência cardíaca. Além disso, doenças valvares, como estenose aórtica ou regurgitação mitral, também podem resultar em insuficiência cardíaca. Outras causas incluem defeitos de condução, arritmia cardíaca e distúrbios infiltrativos / matriciais. Fatores sistêmicos que podem contribuir ou exacerbar a insuficiência cardíaca incluem anemia, hipertireoidismo ou hipertensão. Características radiográficas Radiografia simples Os achados de radiografia de tórax incluem derrames pleurais , cardiomegalia (aumento da silhueta cardíaca), linhas de Kerley B (linhas horizontais na periferia dos campos pulmonares posteriores posteriores), congestão venosa pulmonar no lobo superior e edema intersticial. Ecocardiografia O ultra-som fornece uma avaliação das dimensões das câmaras cardíacas, função valvular, fração de ejeção, efusões pericárdicas e hipertrofia ventricular esquerda. Tratamento e prognóstico O prognóstico geralmente é ruim, a menos que a causa subjacente seja revertida. Como resultado, os pacientes geralmente se deterioram gradualmente com episódios de descompensação aguda e, finalmente, morte. Além de tratar a causa subjacente da insuficiência cardíaca, o tratamento é direcionado a mudanças na dieta e no estilo de vida, medicamentos como inibidores da ECA ou betabloqueadores e, se apropriado, cardioversor desfibrilador implantável (CDI) ou terapia de ressincronização cardíaca (TRC). https://radiopaedia.org/articles/heart-failure-basic #info#"
                                                               "#bloquear_img#screenshot-radiopaedia.org-2018.06.06-13-24-55.png#bloquear_img#"
                                                               "#con#Insuficiência cardíaca#con#"
                                                               "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        menu = wx.Menu("Calcifications")
        menu_pat.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Constructive pericarditis", "#r#Diffuse pericardial calcification seen along the lateral and inferior left wall of the heart, finding raises the diagnostic hypothesis of constrictive pericarditis.#r#"
                                                   "#info#Constrictive pericarditis (or perhaps better called pericardial constriction) is a type of pericarditis that leads to diastolic dysfunction and possible symptoms of right heart failure. The clinical presentation is dominated by ventricular restricted diastolic filling, resulting in an increase in diastolic pressure in all four heart chambers. Patients usually have symptoms of left and right heart failure, including: dyspnea ortopnea easy fatigability hepatomegaly ascites Pathology: Characterized by fibrous constrictive thickening or calcifying of the pericardium , which prevents normal diastolic heart filling. It can follow any type of pericardial effusion and can develop within a variable period of time ranging from two or three months to several years. Idiopathic etiology (most common) 6 previous heart surgery (second most common) 6 radiotherapy (third most common) 6 tuberculosis infection (previously common) 7 viral infection pyogenic sarcoidosis chronic renal failure rheumatic fever (rare) systemic lupus erythematosus (rare) Radiographic features Simple radiography In approximately 50% of cases, pericardial calcification is visible on chest radiographs.  Echocardiography In addition to pericardial thickening, echocardiography may show small tube-shaped ventricles, ventricular septum distortion (e.g. flat or sigmoid-shaped), and atypical septal movement (i.e., septal rebound).  Chest CT - cardiac CT is very sensitive in demonstrating pericardial calcification, which is suggestive of the disease if found in the appropriate clinical setting. A thickened pericardium (more than 4 mm) by itself does not indicate constrictive pericarditis 8 . Contrast CT may also show signs of heart failure, such as septal flattening and contrast retrograde flow in the dilated inferior vena cava and hepatic veins. Cardiac magnetic resonance imaging The pericardium is often thickened to more than 4 mm. MRI is better than CT in the differentiation between pericardial fluid and thickened pericardium 8 . Cine MRI can also demonstrate septal flattening and septal rebound . Treatment and prognosis Constructive pericardiectomy is potentially curable by a pericardiectomy. Differential diagnosis Clinically, it is difficult to differentiate between constrictive pericarditis and restrictive cardiomyopathy. It is important to distinguish between constrictive pericarditis and restrictive cardiomyopathy, as the former benefits from pericardial decapitation. https://radiopaedia.org/articles/constrictive-pericarditis#info#"
                                                   "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-20-43-31.png#bloquear_img#"
                                                   "#con#Hypothesis of constrictive pericarditis can be raised, due to the finding of peripheral calcifications.#con#"
                                                   "#webvideo#https://youtu.be/bgUe8HTgI1Q#webvideo#")

        menu.Append(-1, "area of acute myocardial infarction of the left ventricle", "#r#Myocardial calcifications are observed following the contour of the left ventricle, possibly sequelar to myocardial infarction.#r#"
                                    "#info#In this case, there are calcifications that look like pericardial calcifications, but these are myocardial calcifications in an infarcted area of the left ventricle. Note that they follow the outline of the left ventricle.#info#"
                                    "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-20-50-19.png#bloquear_img#"
                                    "#con#Myocardial calcifications that follow the contour of the left ventricle, possibly sequelar to the myocardial infarction, are noted.#con#"
                                    "#webvideo#https://youtu.be/bgUe8HTgI1Q#webvideo#")
        menu = wx.Menu("Pneumopericardium")
        menu_pat.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Air density inside the pericardium", "#r#Air density inside the pericardium. Find compatible with pneumopericardium.#r#"
                                                                "#webvideo#https://youtu.be/ywR4b5JhT-Q#webvideo#")

        menu.Append(-1, "Continuous diaphragm signal", "#r#Bright strip on the lower edge of the heart. Find suggestive of pneumopericardium.#r#"
                                                       "#webvideo#https://youtu.be/AFZtL9OCiIs#webvideo#")

        menu = wx.Menu("Valve prosthesis")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "tricuspid", "#r#Tricuspid valve prosthesis.#r#"
                                      "#info#The location of the heart valves is best determined by lateral radiography. A line is drawn on the lateral carina radiograph for the cardiac apex. The pulmonary and aortic valves are usually located above this line and the tricuspid and mitral valves are below this line. In this lateral view you can get a good impression of the enlargement of the left atrium.#info#"
                                      "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-19-25-53.png#bloquear_img#"
                                      "#con#Note valve prosthesis.#con#"
                                      "#webvideo#https://youtu.be/Pxc_U5M2uAc#webvideo#")

        menu.Append(-1, "pulmonary", "#r#Pulmonary valve prosthesis.#r#"
                                    "#info#The location of the heart valves is best determined by lateral radiography. A line is drawn on the lateral carina radiograph for the cardiac apex. The pulmonary and aortic valves are usually located above this line and the tricuspid and mitral valves are below this line. In this lateral view you can get a good impression of the enlargement of the left atrium.#info#"
                                    "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-19-25-53.png#bloquear_img#"
                                    "#con#Valve prothesis is observed.#con#"
                                    "#webvideo#https://youtu.be/Pxc_U5M2uAc#webvideo#")

        menu.Append(-1, "mitral", "#r#Mitral valve prosthesis.#r#"
                                  "#info#The location of the heart valves is best determined by lateral radiography. A line is drawn on the lateral carina radiograph for the cardiac apex. The pulmonary and aortic valves are usually located above this line and the tricuspid and mitral valves are below this line. In this lateral view you can get a good impression of the enlargement of the left atrium.#info#"
                                  "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-19-25-53.png#bloquear_img#"
                                  "#con#Valve prothesis is observed.#con#"
                                  "#webvideo#https://youtu.be/Pxc_U5M2uAc#webvideo#")

        menu.Append(-1, "aortic", "#r#Aortic valve prosthesis.#r#"
                                   "#info#The location of the heart valves is best determined by lateral radiography. A line is drawn on the lateral carina radiograph for the cardiac apex. The pulmonary and aortic valves are usually located above this line and the tricuspid and mitral valves are below this line. In this lateral view you can get a good impression of the enlargement of the left atrium.#info#"
                                   "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-19-25-53.png#bloquear_img#"
                                   "#con#Valve prothesis is observed.#con#"
                                   "#webvideo#https://youtu.be/Pxc_U5M2uAc#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "valve prosthesis | Do not specify", "#r#Ring radiopaque image projected in the cardiac shadow, which may correspond to a valve prosthesis.#r#"
                                                            "#webvideo#https://youtu.be/Pxc_U5M2uAc#webvideo#")


        menu_pat.Append(-1, "pericardial effusion", "#r#Enlarged cardiac silhouette with globular shape, profile chest radiography shows a vertical opaque line (pericardial fluid) separating a vertical line directly behind the sternum (epicardial fat) anteriorly from a similar vertical radiotransparent line (pericardial fat) posteriorly; this is known as the oreo biscuit sign, these signs raise the hypothesis of pericardial effusion.#r#"
                                                                               "#info#Pericardial effusion Dr. Dan J Sino and A.Prof Frank Gaillard et al. Pericardial effusions occur when excess fluid accumulates in the pericardial space (a normal pericardial sac contains approximately 30 to 50 ml of fluid). Epidemiology There is not a single demographic group affected, as there are many underlying causes of a pericardial effusion. Clinical presentation The clinical presentation of pericardial effusions is not so much related to the size of the effusion, but to the speed with which the fluid has accumulated, as the slow gradual accumulation allows the pericardium to stretch and accommodate much larger volumes of fluid 4. Regardless of volume, symptoms are related to impaired cardiac function, due to intrapericardial pressure approaching intracardiac pressure, leading to poor filling of the low pressure chambers, particularly the right atrium. Dyspnea and reduced exercise tolerance will be early signs, progressing to compromised severe cardiac output and death in severe cases (for example, cardiac tamponade). Pathology Idiopathic inflammatory etiology post-myocardial infarction: Dressler syndrome bacterial connective tissue disorders bacterial viral tuberculosis post-surgical tuberculosis / trauma pulmonary arterial hypertension 7 radiotherapy primary malignancy, for example, pericardial mesothelioma metastatic endocrine hypothyroidism 3 Radiographic features Radiography a very small pericardial stroke may be hidden in simple films there may be a globular increase in cardiac shadow giving a water bottle configuration lateral chest X-ray may show an opaque vertical line (pericardial fluid) separating a vertical vertical line directly behind the sternum (epicardial fat) previously from a line vertical lucent (pericardial fat) similar afterwards; this is known as the Oreo cookie signal 5 the widening of the subcarinal angle without other evidence of enlargement of the left atrium may be an indirect clue 2 a sign of differential density at the cardiac borders has been suggested 9, but its specificity is limited generally requires more than 200 mL of pericardial fluid to make it visible radiographically Echocardiography Echocardiography is the method of choice to confirm the diagnosis, estimate the volume of fluid and, more importantly, assess the hemodynamic impact of the effusion. CT The accepted thickness of a normal pericardium, measured on computed tomography and magnetic resonance images, is often performed at 2 mm 6. CT makes the diagnosis extremely easy, but it is usually obtained to try to clarify the cause of a stroke instead of confirming the diagnosis. Pericardial effusions are frequent incidental findings in unwell hospitalized patients. Fluid density material is seen around the heart. Careful inspection of the region is necessary to ensure that no invasive masses can be identified. Estimating the volume The depth of the stroke can be used to estimate the probable volume of fluid, as long as the fluid is relatively evenly spread across the pericardium (global stroke) 4. This clearly does not apply to localized effusions. <5 mm: 50-100 mL 5-10 mm: 100-250 mL 10-20 mm: 250-500 mL> 20 mm:> 500 mL Treatment and prognosis If small, asymptomatic and clinically unsuspecting, conservative treatment is usually favored. If it is large, symptomatic, or there is a clinical concern for the underlying cause (eg, infection, malignancy), pericardiocentesis can be performed to drain the fluid. A Seldinger technique is employed, usually under ultrasound / echocardiographic guidance, to insert a drain into the pericardial space 4. In cases where effusions are recurrent and symptomatic (for example, malignancy), pericardial fenestration can be performed. Differential diagnosis of hemopericardium: it has greater attenuation on CT and often a different clinical context than cardiomegaly: it can sometimes imitate a stroke.  https://radiopaedia.org/articles/pericardial-effusion #info#"
                                                                               "#bloquear_img#screenshot-radiopaedia.org-2018.06.06-16-12-33.png#bloquear_img#"
                                                                               "#con#Pericardic effusion.#con#"
                                                                               "#webvideo#https://youtu.be/VjYQOO44Yx0#webvideo#")

        self.menu_coracao.AppendSeparator()
        menu = wx.Menu("Cardiac Pacemaker")
        menu.Append(-1,"projected on the right hemithorax." ,"#r#Cardiac pacemaker projected on the right hemithorax.#r#"
                                                          "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        menu.Append(-1,"projected on the left hemithorax." ,"#r#Cardiac pacemaker projected on the left hemithorax.#r#"
                                                           "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)

        menu = wx.Menu("Medical supplies")
        submenu1 = wx.Menu("Port-A-Cath type catheter")
        submenu2 = wx.Menu("projected on the right hemithorax")
        submenu1.Append(-1, submenu2.GetTitle(), submenu2)
        submenu2.Append(-1, "with the distal end projected in the superior vena cava.", "#r#Port-A-Cath type catheter, projected in the right hemithorax, with the distal end projected in the superior vena cava.#r#"
                                                                                         "#webvideo#https://youtu.be/xVebbriPQAs#webvideo#")
        submenu2.Append(-1, "with the distal end projected into the right atrium.", "#r#Port-A-Cath type catheter, projected on the right hemithorax, with the distal end projected on the right atrium.#r#"
                                                                                    "#webvideo#https://youtu.be/xVebbriPQAs#webvideo#")
        submenu2 = wx.Menu("projected on the left hemithorax")
        submenu1.Append(-1, submenu2.GetTitle(), submenu2)
        submenu2.Append(-1, "with the distal end projected in the superior vena cava.", "#r#Port-A-Cath type catheter, projected in the left hemithorax, with the distal end projected in the superior vena cava.#r#"
                                                                                         "#webvideo#https://youtu.be/xVebbriPQAs#webvideo#")
        submenu2.Append(-1, "with the distal end projected into the right atrium.", "#r#Port-A-Cath type catheter, projected in the left hemithorax, with the distal end projected in the right atrium.#r#"
                                                                                    "#webvideo#https://youtu.be/xVebbriPQAs#webvideo#")
        menu.Append(-1, submenu1.GetTitle(), submenu1)
        menu.Append(-1,"Electrodes", "#r#Presence of cardiac monitoring electrodes.#r#"
                                    "#webvideo#https://youtu.be/kwLbSx9BNbU#webvideo#")
        menu.Append(-1,"Electrodes and ventilation equipment" ,"#r#Presence of cardiac monitoring electrodes and ventilation material.#r#"
                                                             "#webvideo#https://youtu.be/kwLbSx9BNbU#webvideo#")
        menu.Append(-1,"Self-adhesive electrodes" ,"#r#Presence of self-adhesive cardiac monitoring electrodes.#r#"
                                                  "#webvideo#https://youtu.be/kwLbSx9BNbU#webvideo#")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat

    def atrium(self, x=1, y=1, largura=1, altura=1, nome_anat ="left atrium"):
        """Return custom button. must define
        the position by x and y."""

        nome_anat_ex_direita = nome_anat.split()[1].replace("right", "right").replace("left", "left")

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0] + nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0]+ nome_anat[1:])
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Normal | right atrium", "#r#Right atrium with preserved size and good outline of its silhouette.#r#"
                                                               "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Increased | left atrium | Double contour sign", "#r#There is a double left atrial contour and cranial displacement of the ipsilateral bronchus, signs compatible with an increase in the left atrium.#r#"
                                                                                             "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Increased | right atrium","#r#Increased convexity of the atrial border, distance from the right border of the heart in relation to the spine, alteration of the cardiophrenic angle and posterior displacement of the inferior vena cava.#r#"
                                                                 "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Consolidation")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Silhouette sign | consolidation", "#r#The edge" + nome_anat_ex_direita + " of the heart (edge of " + nome_anat + ") is obscured by the consolidation process.#r#"
                                                              "#info#Consolidation of the right middle lobe The right edge of the heart (edge of the right atrium) is obscured Consolidation (asterisk) is limited above by a sharp line, formed by the horizontal fissure The pathology must therefore involve the right middle lobe More extensive shading as well involves the right and left perihilar regions Clinical information Child with cough and fever Diagnosis Pneumonia involving the right middle lobe#info#"
                                                              "#con#Pulmonary consolidation.#con#"
                                                              "#bloquear_img#screenshot-www.radiologymasterclass.co.uk-2018.07.21-21-52-44.png#bloquear_img#"
                                                              "#webvideo#https://youtu.be/Gd7X2oI6iKc#webvideo#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


    # =-=-=-=-=-=-=  Novo Padrão -=-=-=-=-=-=-=-=-=-=-=-=

    def hilo(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="hilo"):
        """Return custom button. must define
        the position by x and y."""

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0]+ nome_anat[1:])
        self.menu_coracao.Append(-1, "Pulmonary hilos without changes.", "#r#Pulmonary hilos without changes.#r#"
                                                                         "#webvideo#https://youtu.be/mJZRZUBnYqY#webvideo#")
        self.menu_coracao.AppendSeparator()
        menu = wx.Menu("Prominence of pulmonary hilos")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)

        menu.Append(-1, "Hilo's slight prominence " + nome_anat.split()[0] + ". It may be associated with some degree of inflammatory bronchopathy.", "#r#Hilo's slight prominence " + nome_anat.split()[0] + ". It may be associated with some degree of inflammatory bronchopathy.#r#"
                                                                                                                                                                                                               "#webvideo#https://youtu.be/HZlOWgurwe8#webvideo#")
        menu.Append(-1, "Tenuous bilateral hilar prominence, which may be associated with some degree of inflammatory bronchopathy.", "#r#Tenuous bilateral hilar prominence, which may be associated with some degree of inflammatory bronchopathy.#r#"
                                                                                                                                 "#webvideo#https://youtu.be/HZlOWgurwe8#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Prominent pulmonary hilum " + nome_anat.split()[0] + ".. It may be associated with some degree of inflammatory bronchopathy.", "#r#Proeminência do hilo " + nome_anat.split()[0] + ". It may be associated with some degree of inflammatory bronchopathy.#r#"
                                                                                                                                                                                                   "#webvideo#https://youtu.be/HZlOWgurwe8#webvideo#")
        menu.Append(-1, "Proeminência hilar bilateral,. It may be associated with some degree of inflammatory bronchopathy.", "#r#Proeminência hilar bilateral. It may be associated with some degree of inflammatory bronchopathy.#r#"
                                                                                                                           "#webvideo#https://youtu.be/HZlOWgurwe8#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Prominence of pulmonary hilum.", "#r#Prominence of pulmonary hilum.#r#"
                                                              "#info#Here are some more examples of sarcoidosis.  Click to enlarge. Lymphadenopathy and groundglass appearance of lungs Lymphadenopathy, Sign 1-2-3 Bulky Lymphadenopathy Sign 1-2-3 Nodular lung pattern, no lymphadenopathy Hilar lymphadenopathy and paratracheal lymphadenopathy#info#"
                                                              "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-09-48-59.png#bloquear_img#"
                                                              "#con#Prominence of pulmonary hilos.#con#"
                                                              "#webvideo#https://youtu.be/HZlOWgurwe8#webvideo#")

        menu.Append(-1, "Prominent pulmonary hilum " + nome_anat.split()[0] + ".", "#r#"+ "Prominent pulmonary hilum " + nome_anat.split()[0] + "." +"#r#"
                                                                                    "#info#Increased hili is usually due to lymphadenopathy or enlarged vessels. In this case, there is an increased hilar shadow on both sides.  This could be the result of enlarged vessels or enlarged lymph nodes.  A very useful finding in this case is the mass to the right of the trachea. This is known as the 1-2-3 sign in sarcoidosis, i.e. enlargement of the left hilum, right hilum and paratracheal.#info#"
                                                                                    "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-09-43-22.png#bloquear_img#"
                                                                                    "#con#"+ "Prominence of lung hilum " + nome_anat.split()[0] + "." +"#con#"
                                                                                    "#webvideo#https://youtu.be/HZlOWgurwe8#webvideo#")
        self.menu_coracao.AppendSeparator()


        self.menu_coracao.Append(-1, "Residual calcifications", "#r#Residual calcifications in the hilar zones.#r#"
                                                                "#webvideo#https://youtu.be/HZlOWgurwe8#webvideo#")

        menu = wx.Menu("Discrete peribronchial thickening")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "bilateral, and may be related to...","#r#Discrete bilateral peribronchial thickening, which may be related to inflammatory / infectious bronchopathy. Correlate to clinical and/or laboratory data.#r#"
                                                                  "#webvideo#https://youtu.be/HZlOWgurwe8#webvideo#")
        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


    def aorta(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="aorta"):
        """Return custom button. must define
        the position by x and y."""

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0]+ nome_anat[1:])
        self.menu_coracao.Append(-1, "Normal thoracic aorta.", "#r#Normal thoracic aorta.#r#"
                                                               "#webvideo#https://youtu.be/GCF8Y71cXFU#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Describe\tOptions", "#r#Thoracic aorta #descrever_aorta# #r#"
                                                          "#webvideo#https://youtu.be/mEGTzW6k2ww#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Thoracic aorta with impaired evaluation.", "#r#Thoracic aorta with impaired evaluation.#r#"
                                                                                  "#webvideo#https://youtu.be/GCF8Y71cXFU#webvideo#")
        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat

    def lung(self, x=1, y=1, largura=1, altura=1, nome_anat ="lung"):
        """Retorna botão customizado. deve definir
        a posição por x e y."""

        nome_anat_ex_direita = nome_anat.split()[1].replace("right", "right").replace("left", "left")

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0]+ nome_anat[1:])
        menu = wx.Menu("Technique")
        submenu1_1 = wx.Menu("Positioning")
        submenu1_2 =  wx.Menu("Technically appropriate")
        menu.Append(-1, submenu1_1.GetTitle(), submenu1_1)
        menu.Append(-1, submenu1_2.GetTitle(), submenu1_2)

        submenu1_1.Append(-1, "PA e Lateral", "#r#Chest X-ray in PA and left side.#r#"
                                              "#info#Posterioranterior and Lateral: The standard thoracic examination consists of a posterior (posterioranterior) and lateral thoracic radiograph. The films are read together. The PA exam is seen as if the patient were standing in front of him/her with the right side to his/her left. The patient is facing to the left in lateral view. Comparison films can be invaluable ??- Old Gold! If you have comparison films, the old PA film is shown next to the new PA film and the old side is shown adjacent to the new side.#info#"
                                              "#bloquear_img#screenshot-www.google.com.br-2018.06.07-10-11-16.png#bloquear_img#"
                                              "#con#Chest X-ray in PA and left side.#con#"
                                             "#webvideo#https://youtu.be/7v9GKt69Z-M#webvideo#")
        submenu1_1.AppendSeparator()

        submenu1_1.Append(-1, "PA", "#r#Chest X-ray in PA.#r#"
                                    "#info#Chest Radiography in PA: This is the most used incidence in simple chest radiography. As the X-rays are divergent, so that the structures do not suffer excessive magnification, a minimum distance of 1.50 m is necessary for their performance. The ideal distance is 1.80 m. The X-ray beams enter later, through the back of the patient, and the anterior portion of the thorax is in contact with the radiological film. This position is performed for two reasons: it avoids the magnification of the heart, which, because it is anterior, is close to the film; it allows the positioning of the shoulders in such a way that the scapula is outside the film. #info#"
                                    "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-10-17-48.png#bloquear_img#"
                                    "#con#Chest X-ray in PA.#con#"
                                    "#webvideo#https://youtu.be/7v9GKt69Z-M#webvideo#")


        submenu1_1.Append(-1, "lateral", "#r#Left side chest radiography#r#"
                                        "#info#The lateral view should always be requested and performed, together with the BP. It helps a lot in the location and characterization of injuries. The left side is routinely performed, that is, with the left side in contact with the film and with the beam entrance on the right (figure 5), so as not to magnify the heart. The right side is performed in exceptional cases to assess injuries on the right.#info#"
                                        "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-10-21-54.png#bloquear_img#"
                                        "#con#Left side chest radiography.#con#"
                                        "#webvideo#https://youtu.be/7v9GKt69Z-M#webvideo#")


        submenu1_1.Append(-1, "AP", "#r#AP chest X-ray#r#"
                                    "#info#Anteroposterior (AP): This view is performed with the posterior portion of the chest in contact with the film; the X-ray beam enters previously. However, as the heart is far from the film, it is magnified, making it difficult to analyze its size and also the adjacent pulmonary segments (medial of the middle lobe and lingula). This incidence, therefore, occurs only in special cases, when the patient is unable to remain in the orthostatic position: young children and debilitated or bedridden patients.#info#"
                                    "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-10-24-59.png#bloquear_img#"
                                    "#con#AP chest X-ray.#con#"
                                    "#webvideo#https://youtu.be/7v9GKt69Z-M#webvideo#")

        submenu1_1.Append(-1, "AP and supine position", "#r#Chest X-ray in AP and supine position.#r#"
                                    "#info#Anteroposterior (AP): This view is performed with the posterior portion of the chest in contact with the film; the X-ray beam enters previously. However, as the heart is far from the film, it is magnified, making it difficult to analyze its size and also the adjacent pulmonary segments (medial of the middle lobe and lingula). This incidence, therefore, occurs only in special cases, when the patient is unable to remain in the orthostatic position: young children and debilitated or bedridden patients.#info#"
                                    "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-10-24-59.png#bloquear_img#"
                                    "#con#AP chest X-ray.#con#"
                                    "#webvideo#https://youtu.be/7v9GKt69Z-M#webvideo#")


        submenu1_1.Append(-1, "Apic-lordotic", "#r#Apical-lordotic chest radiography.#r#"
                                                 "#info#The X-ray beam enters previously and the back is in contact with the film. The patient takes a position in hyperlordosis, removing the collarbones from the fields. This incidence is of great value for the assessment of pulmonary apexes, middle lobe and lingula#info#"
                                                 "#bloquear_img#screenshot-www.google.com.br-2018.06.07-10-32-23.png#bloquear_img#"
                                                 "#con#Chest radiography in apical-lordotic view.#con#"
                                                 "#webvideo#https://youtu.be/bcPOx08so7A#webvideo#")
        submenu1_1.AppendSeparator()



        submenu1_1.Append(-1, "Right lateral decubitus",
                          "#r#Chest radiography in the right lateral position with horizontal rays.#r#"
                                                  "#info#This incidence lends itself basically to differentiate between effusion and pleural thickening. The patient is placed in the lateral decubitus position, lying on the hemithorax to be examined, and the bundle enters in a horizontal direction.#info#"
                                                  "#bloquear_img#screenshot-www.google.com.br-2018.06.07-10-43-15.png#bloquear_img#"
                                                  "#con#Radiography of the chest in lateral decubitus with horizontal rays.#con#"
                                                  "#webvideo#https://youtu.be/CVimots4lGA#webvideo#")

        submenu1_1.Append(-1, "Left lateral decubitus",
                          "#r#Chest radiography in left lateral decubitus with horizontal rays.#r#"
                          "#info#This incidence lends itself basically to differentiate between effusion and pleural thickening. The patient is placed in the lateral decubitus position, lying on the hemithorax to be examined, and the bundle enters in a horizontal direction.#info#"
                          "#bloquear_img#screenshot-www.google.com.br-2018.06.07-10-43-15.png#bloquear_img#"
                          "#con#Radiography of the chest in lateral decubitus with horizontal rays.#con#"
                          "#webvideo#https://youtu.be/CVimots4lGA#webvideo#")
        submenu1_1.AppendSeparator()


        submenu1_1.Append(-1, "Oblique incidence",
                          "#r#Chest radiography with oblique view.#r#"
                          "#info#Oblique views can be performed to better locate or characterize lesions partially covered by other structures.#info#"
                          "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-10-48-53.png#bloquear_img#"
                          "#con#Chest radiography with oblique view.#con#"
                          "#webvideo#https://youtu.be/7v9GKt69Z-M#webvideo#")


        submenu1_2.Append(-1, "Satisfying inspiration",
                          "#r#Satisfactory inspiration.#r#"
                          "#info#Ideally, the exam should be performed in maximum inspiratory apnea. In order to know if the exam is well inspired, we should have 9 to 11 posterior ribs projecting over the lung fields.#info#"
                          "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-10-57-14.png#bloquear_img#"
                          "#con#Satisfactory inspiration.#con#"
                          "#webvideo#https://youtu.be/5owzpKMKNH0#webvideo#")

        submenu1_2.Append(-1, "Hipoinsuflação pulmonar",
                          "#r#Examination performed with pulmonary hypoinflation.#r#"
                          "#info#Ideally, the exam should be performed in maximum inspiratory apnea. In order to know if the exam is well inspired, we should have 9 to 11 posterior ribs projecting over the lung fields.#info#"
                          "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-10-57-14.png#bloquear_img#"
                          "#con#Pulmonary hypoinflation.#con#"
                          "#webvideo#https://youtu.be/5owzpKMKNH0#webvideo#")

        submenu1_2.Append(-1, "Pulmonary hyperinflation",
                          "#r#Pulmonary hyperinflation, which must be compared with clinical data.#r#"
                          "#info#Ideally, the exam should be performed in maximum inspiratory apnea. In order to know if the exam is well inspired, we should have 9 to 11 posterior ribs projecting over the lung fields.#info#"
                          "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-10-57-14.png#bloquear_img#"
                          "#con#Pulmonary hyperinflation.#con#"
                          "#webvideo#https://youtu.be/5owzpKMKNH0#webvideo#")
        submenu1_2.AppendSeparator()

        submenu1_2.Append(-1, "Adequate X-ray penetration.",
                          "#r#Adequate X-ray penetration.#r#"
                          "#info#Proper radiation penetration of the patient is also necessary for a good film. In a good PA film, the disc spaces in the thoracic spine should be barely visible through the heart, but the bone details in the spine are generally not seen. On the other hand, penetration is sufficient for bronchovascular structures to be seen through the heart. In the side view, you can look for proper penetration and inspiration, noting that the spine seems to darken as you move caudally. This is due to more air in the lung in the lower lobes and less in the chest wall. The sternum should be seen from the edge and then you should see two pairs of ribs.#info#"
                          "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-11-12-25.png#bloquear_img#"
                          "#con#Adequate X-ray penetration.#con#"
                          "#webvideo#https://youtu.be/AiPT-691m0k#webvideo#")

        submenu1_2.Append(-1, "Radiography poorly penetrated",
                          "#r#Radiography poorly penetrated.#r#"
                          "#info#Proper radiation penetration of the patient is also necessary for a good film. In a good PA film, the disc spaces in the thoracic spine should be barely visible through the heart, but the bone details in the spine are generally not seen. On the other hand, penetration is sufficient for bronchovascular structures to be seen through the heart. In the side view, you can look for proper penetration and inspiration, noting that the spine seems to darken as you move caudally. This is due to more air in the lung in the lower lobes and less in the chest wall. The sternum should be seen from the edge and then you should see two pairs of ribs.#info#"
                          "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-11-12-25.png#bloquear_img#"
                          "#con#Radiography poorly penetrated.#con#"
                          "#webvideo#https://youtu.be/AiPT-691m0k#webvideo#")

        submenu1_2.Append(-1, "Very penetrated radiography",
                          "#r#Radiography poorly penetrated.#r#"
                          "#info#Proper radiation penetration of the patient is also necessary for a good film. In a good PA film, the disc spaces in the thoracic spine should be barely visible through the heart, but the bone details in the spine are generally not seen. On the other hand, penetration is sufficient for bronchovascular structures to be seen through the heart. In the side view, you can look for proper penetration and inspiration, noting that the spine seems to darken as you move caudally. This is due to more air in the lung in the lower lobes and less in the chest wall. The sternum should be seen from the edge and then you should see two pairs of ribs.#info#"
                          "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-11-12-25.png#bloquear_img#"
                          "#con#Radiography very penetrated.#con#"
                          "#webvideo#https://youtu.be/AiPT-691m0k#webvideo#")
        submenu1_2.AppendSeparator()



        submenu1_2.Append(-1, "Rotation | Well-aligned exam",
                          "#r#Exam well aligned.#r#"
                          "#info#For the examination to be well centered, the medial edges of the clavicles must be equidistant from the center of the spine. In addition, the shoulder blades must be out of the field.#info#"
                          "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-11-19-34.png#bloquear_img#"
                          "#con#Exam well aligned.#con#"
                          "#webvideo#https://youtu.be/DOUv7ya6wco#webvideo#")

        submenu1_2.Append(-1, "Rotation | Radiography poorly centered.",
                          "#r#Radiography poorly centered.#r#"
                          "#info#For the examination to be well centered, the medial edges of the clavicles must be equidistant from the center of the spine. In addition, the shoulder blades must be out of the field.#info#"
                          "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-11-19-34.png#bloquear_img#"
                          "#con#Radiography poorly centered.#con#"
                          "#webvideo#https://youtu.be/DOUv7ya6wco#webvideo#")

        submenu1_2.Append(-1, "Right rotation | poorly centered.",
                          "#r#Radiographs poorly centered, rotated to the right.#r#"
                          "#info#For the examination to be well centered, the medial edges of the clavicles must be equidistant from the center of the spine. In addition, the shoulder blades must be out of the field.#info#"
                          "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-11-19-34.png#bloquear_img#"
                          "#con#Radiographs poorly centered, rotated to the right.#con#"
                          "#webvideo#https://youtu.be/DOUv7ya6wco#webvideo#")

        submenu1_2.Append(-1, "Left rotation | poorly centered.",
                          "#r#Radiographs poorly centered, rotated to the left.#r#"
                          "#info#For the examination to be well centered, the medial edges of the clavicles must be equidistant from the center of the spine. In addition, the shoulder blades must be out of the field.#info#"
                          "#bloquear_img#screenshot-professor.pucgoias.edu.br-2018.06.07-11-19-34.png#bloquear_img#"
                          "#con#Radiographs poorly centered, rotated to the left.#con#"
                          "#webvideo#https://youtu.be/DOUv7ya6wco#webvideo#")

        submenu1_2.Append(-1, "Impaired evaluation | positioning.", "#r#Study with impaired evaluation due to positioning.#r#"
                                                                         "#webvideo#https://youtu.be/DOUv7ya6wco#webvideo#")

        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Pulmonary fields")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Pleuro-pulmonary fields with good transparency.", "#r#Pleuro-pulmonary fields with good transparency.#r#"
                                                                           "#webvideo#https://youtu.be/AFZtL9OCiIs#webvideo#")
        menu.Append(-1, "Normal pulmonary vascular network.", "#r#Normal pulmonary vascular network..#r#"
                                                           "#webvideo#https://youtu.be/AFZtL9OCiIs#webvideo#")
        submenu = wx.Menu("Absence of consolidation")
        menu.Append(-1, submenu.GetTitle(), submenu)
        submenu.Append(-1, "Absence of consolidation", "#r#Absences of areas of pulmonary consolidation.#r#"
                                                       "#webvideo#https://youtu.be/Gd7X2oI6iKc#webvideo#")
        submenu.Append(-1, "Absence of gross consolidations", "#r#Absence of areas of gross consolidation in the lung parenchyma.#r#"
                                                                   "#webvideo#https://youtu.be/qms-_ob9Fgs#webvideo#")
        submenu.Append(-1, "No concealment or consolidation", "#r#Absence of areas of concealment or consolidation in the lung parenchyma.#r#"
                                                                    "#webvideo#https://youtu.be/Gd7X2oI6iKc#webvideo#")

        menu.Append(-1, "Other pulmonary segments with satisfactory transparency.", "#r#Other pulmonary segments with satisfactory transparency.#r#"
                                                         "#webvideo#https://youtu.be/AFZtL9OCiIs#webvideo#")
        menu.AppendSeparator()
        submenu1 = wx.Menu("Accentuation of the pulmonary vascular network\tMenu")
        menu.Append(-1, submenu1.GetTitle(), submenu1)
        submenu1.Append(-1, "Accentuation of the pulmonary vascular network.", "#r#Accentuation of the pulmonary vascular network.#r#"
                                                                      "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        submenu1.Append(-1, "Slight accentuation of the pulmonary vascular network.", "#r#Slight accentuation of the pulmonary vascular network.#r#"
                                                                           "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        submenu1.Append(-1, "Important accentuation of the pulmonary vascular network.", "#r#Important accentuation of the pulmonary vascular network.#r#"
                                                                                 "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        submenu1.AppendSeparator()
        submenu1.Append(-1, "Accentuation of the pulmonary vascular network in " + nome_anat + ".", "#r#Accentuation of the pulmonary vascular network in " + nome_anat + ".#r#"
                                                                                            "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        submenu1.Append(-1, "Slight accentuation of the pulmonary vascular network in " + nome_anat + ".", "#r#Slight accentuation of the pulmonary vascular network in " + nome_anat + ".#r#"
                                                                                                      "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        submenu1.Append(-1, "Important accentuation of the pulmonary vascular network in " + nome_anat + ".", "#r#Important accentuation of the pulmonary vascular network in " + nome_anat + ".#r#"
                                                                                                                  "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")

        menu.Append(-1, "Cephalization of the vascular network", "#r#Cephalization of the vascular network, suggesting pulmonary venocapillary congestion.#r#"
                                                         "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Lungs | frosted glass ",
                                 "#r#Lungs with a frosted glass pattern, diffuse and symmetrical, with air bronchograms.#r#"
                                 "#info#Respiratory distress syndrome (RDS) is a relatively common condition resulting from insufficient surfactant production that occurs in premature infants. In images, the condition usually appears as diffuse bilateral frosted glass lungs and relatively symmetrical with low volumes and a bell-shaped chest.#info#"
                                 "#con#Finding may be related to respiratory distress syndrome.#con#"
                                 "#bloquear_img#screenshot-radiopaedia.org-2018.07.15-12-18-28.png#bloquear_img#"
                                 "#webvideo#https://youtu.be/KlVlyt1Bdps#webvideo#")

        self.menu_coracao.Append(-1, "Opacity",
                        "#r#Opacity #descrever_tipo_opacidade# #desc_opa_pulmao_local# " + nome_anat + " " + "#desc_opa_pulmao_hd##r#"
                                                                      "#info#An air bronchogram is a tubular outline of an airway made visible by filling the surrounding alveoli with fluid or inflammatory exudates. Six causes of air bronchograms are; 1. pulmonary consolidation, 2. pulmonary edema, 3. non-obstructive pulmonary atelectasis, 4. severe interstitial disease, 5. neoplasia 6. normal expiration.#info#"
                                                                      "#bloquear_img#screenshot-www.google.com.br-2018.06.06-10-45-19.png#bloquear_img#"
                                                                      "#con#Lung opacity.#con#"
                                                                      "#webvideo#https://youtu.be/fW14iNSapw0#webvideo#")

        menu = wx.Menu("Interstitial")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)

        submenu1 = wx.Menu("Interstitial thickening")
        menu.Append(-1, submenu1.GetTitle(), submenu1)
        submenu1.Append(-1, "diffuse | peribroncovascular " + nome_anat, "#r#Diffuse thickening of the peribroncovascular interstice of " + nome_anat + ", corresponding to an inflammatory / infectious process. Correlate to clinical data.#r#"
                                                                                                                                                        "#webvideo#https://youtu.be/fW14iNSapw0#webvideo#")
        submenu1.Append(-1, "diffuse | bilateral peribroncovascular", "#r#Diffuse thickening of the bilateral peribroncovascular interstice, which may correspond to an inflammatory / infectious process. Correlate to clinical data.#r#"
                                                                     "#webvideo#https://youtu.be/fW14iNSapw0#webvideo#")

        submenu2 = wx.Menu("Interstitial infiltrate")
        menu.Append(-1, submenu2.GetTitle(), submenu2)
        submenu2.Append(-1, "diffuse to " + nome_anat.split()[1].replace("right", "right").replace("left", "left"), "#r#Diffuse pulmonary interstitial infiltrate " + nome_anat.split()[1].replace("right", "right").replace("left", "left") + ", corresponding to an inflammatory / infectious process.#r#"
                                                                                                                                                                                                                                                                     "#webvideo#https://youtu.be/fW14iNSapw0#webvideo#")
        submenu2.Append(-1, "bilateral diffuse", "#r#Diffuse bilateral pulmonary interstitial infiltrate, which may correspond to an inflammatory / infectious process.#r#"
                                                "#webvideo#https://youtu.be/fW14iNSapw0#webvideo#")
        submenu2.AppendSeparator()
        submenu2.Append(-1, "Interstitial edema | Peripheral", "#r#Shading that predominates on the periphery of the lungs, a finding suggestive of interstitial pulmonary edema.#r#"
                                                               "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")

        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Pulmonary nodule", "#r#It is delimited #num_nodulo# radiopaque images, projected #desc_opa_pulmao_local# " + nome_anat + ", #num_medindo# corresponding to a small pulmonary nodule.#r#"
                                                        "#webvideo#https://youtu.be/izqZjLbUFwk#webvideo#")
        self.menu_coracao.AppendSeparator()


        menu = wx.Menu("Pleura | Fissures")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        submenu1 = wx.Menu("Pleura")
        menu.Append(-1, submenu1.GetTitle(), submenu1)

        submenu1.Append(-1, "Peripheral pleural thickening at " + nome_anat_ex_direita + ".", "#r#Peripheral pleural thickening at " + nome_anat_ex_direita + ".#r#"
                                                                                           "#info#Placas pleurais relacionadas ao amianto Sombras irregulares bilaterais e bem definidas, tão densas quanto os ossos Espessamento pleural periférico Informação clínica Falta de ar leve crônica Estivador aposentado com histórico de múltiplas exploradas ao amianto Diagnóstico Placas pleurais relacionadas com o amianto calcificado bilaterais.#info#"
                                                                                           "#con#Peripheral pleural thickening.#con#"
                                                                                           "#bloquear_img#screenshot-www.radiologymasterclass.co.uk-2018.07.21-21-38-09.png#bloquear_img#")

        submenu1.Append(-1, "Bilateral peripheral pleural thickening.", "#r#Bilateral peripheral pleural thickening.#r#"
                                                                      "#info#Asbestos-related pleural plaques Irregular bilateral shadows, as dense as bones Peripheral pleural thickening Clinical information Retired chronic shortness of breath Retired man with a history of multiple asbestos-exposed pleural plaques Diagnosis of bilateral calcified asbestos-related pleural plaques.#info#"
                                                                      "#con#Peripheral pleural thickening.#con#"
                                                                      "#bloquear_img#screenshot-www.radiologymasterclass.co.uk-2018.07.21-21-38-09.png#bloquear_img#")

        submenu_fis = wx.Menu("Fissures")
        menu.Append(-1, submenu_fis.GetTitle(), submenu_fis)
        submenu_fis.Append(-1, "Oblique fissure thickening", "#r#Thickening of the oblique fissure seen on the lateral radiograph.#r#")


        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Anatomical variant")
        self.menu_coracao.Append(-1, "Anatomical variant", menu)
        menu.Append(-1, "Azygos lobe", "#r#Fine vertical linear opacity is observed, ending in a small rounded opacity, projected in the upper field of the right hemithorax, found compatible with the lobe of the azygos vein.#r#"
                                               "#info#The azygos vein lobe is an anatomical variant that appears in 0.1 to 8% of individuals in general and results from the anomalous development of the upper lobe of the right lung. In its majority it has no clinical implications."
                                               " It is created when a laterally displaced azygos vein makes a deep fissure in the upper part of the lung.#info#"
                                               "#con#The azygos vein lobe is an anatomical variant of the development of the upper lobe of the right lung, most of it has no clinical implications.#con#"
                                               "#bloquear_img#screenshot-www.scielo.mec.pt-2018.06.03-12-42-09.png#bloquear_img#"
                                               "#webvideo#https://youtu.be/ZnkNWUAnXsE#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Pneumothorax | Hemothorax")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "There is no sign of pneumothorax and hemothorax.", "#r#There is no sign of pneumothorax and hemothorax.#r#"
                            "#webvideo#https://youtu.be/7rNYjiRAImk#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Pneumothorax",
                                 "#r#Visceral pleural border visible as a very thin white line in " + nome_anat + ". It can be a pneumothorax.#r#"
                                 "#info#The retracted visceral pleura is seen, which indicates a pneumothorax. There is a visible horizontal line (yellow arrow). Normally, there are no straight lines in the human body unless there is a level of air fluid. This means there is a hydro-pneumothorax. When a pneumothorax is small, this air-liquid level may be the only key to diagnosis of a pneumothorax. Pneumothorax Dr. Rohit Sharma and Dr. Martin Gorrochategui et al. Pneumothorax refers to the presence of gas (air) in the pleural space. When this collection of gases is constantly increasing with the resulting compression of mediastinal structures, it can be fatal and is known as a hypertensive pneumothorax. For pneumothorax that occur in newborns, see the article on neonatal pneumothorax . Epidemiology There are many causes of pneumothorax that make it impossible to generalize epidemiology. However, primary spontaneous pneumothorax occurs in younger patients (usually under 35 years of age), while secondary spontaneous pneumothorax occurs in older patients (usually over 45 years of age) 4 .  Clinical presentation The presentation is variable and can vary from absence of symptoms to severe dyspnea with tachycardia and hypotension. In patients with hypertensive pneumothorax, the presentation may be with distended neck veins and tracheal deviation, cardiac arrest and, in more severe cases, death. It is interesting to note that some generalizations can be made regarding the clinical presentation in primary versus secondary spontaneous pneumothorax: primary spontaneous: pleuritic chest pain usually present, mild or moderate secondary spontaneous dyspnea: pleuritic chest pain often absent, dyspnea usually severe Pathology It is useful to divide the pneumothorax into three categories 4 : Primary spontaneous: no underlying secondary spontaneous lung disease: iatrogenic / traumatic underlying lung disease Primary spontaneous pneumothorax is that which occurs in a patient with no known underlying lung disease. Tall, thin people are more likely to develop a spontaneous primary pneumothorax. There may be a familiar component and there are well-known associations 10 : Marfan's syndrome Ehlers-Danlos syndrome Alpha-1-antitrypsin deficiency Spontaneous Secondary When the underlying lung is abnormal, a pneumothorax is referred to as secondary spontaneous. There are many lung diseases that predispose to pneumothorax, including: cystic lung disease blisters, blebs emphysema, Pneumocystis jiroveci (PJP) faveolamento asthma: interstitial lung disease at terminal stage lymphangiomyomatosis (LAM) Langerhans cell histiocytosis (LCH) due to apical lung changes of ankylosing spondylitis 1 c fibrosis ystic necrosis parenchymatous abscess, necrotic pneumonia, septic emboli, fungal disease, tuberculosis, cavitating neoplasia, metastatic osteogenic sarcoma, radiation necrosis, pulmonary infarction of other catamenial pneumothorax 2,4 : recurrent spontaneous pneumothorax during menstruation, associated with rarely fibroelastosis pleura endometriosis 9 Iatrogenic / traumatic causes include 1-4 : iatrogenic: barotrauma percutaneous biopsy, radiofrequency (RF) ablation ventilator of the endoscopic oesophagus traumatic perforation: lung tear tracheobronchial rupture acupuncture esophageal rupture Other pneumoperitoneum passing through congenital / acquired diaphragmatic defects Radiographic features Thoracic radiography A pneumothorax is when sought, usually relatively appreciated. Usually they show: visible visceral pleural border is seen as a very thin and pointed white line no lung mark is seen peripheral to this peripheral space line is radiolucent compared to the adjacent lung may collapse completely the mediastinum should not move away from the pneumothorax unless a hypertensive pneumothorax is present (discussed separately). Subcutaneous emphysema and pneumomediastinum may also be present In cases where these characteristics are not clearly present, several techniques can be employed: lateral decubitus radiography: the suspect side should be taken and the lung will then 'fall' from the chest wall expiratory chest radiography: lung becomes smaller and denser the pneumothorax remains the same size and therefore is more evident: although some authors suggest that there is no difference in detection rate 6 Computed Tomography When imagined, detection in supine can be difficult: see the pneumothorax in a patient in dorsal decubitus position and the pneumothorax is one of the causes of a transradiant hemithorax . Ultrasound The M mode can be used to determine the movement of the lung within the space between the ribs. Small pneumothorax are best appreciated previously in the supine position (gas rises), while large pneumothorax are appreciated laterally in the middle axillary line. See: ultra sound for CT pneumothorax Since the windows of the lungs are examined, a pneumothorax is easily identified at CT, and should not essentially represent any diagnostic difficulty. When a bullous disease is present, a localized pneumothorax may appear similar. Treatment and prognosis Treatment depends on several factors: size of the pneumothorax background lung disease / respiratory reserve symptoms These can be used together to determine the best course of action. The following guidelines are based on the British Thoracic Society guidelines for the treatment of pneumothorax; local protocol may be different: small-bordered (<2 cm) asymptomatic pneumothorax: no treatment with follow-up radiology to confirm pneumothorax resolution with mild symptoms (no underlying lung condition): needle aspiration at first instance pneumothorax in a patient with chronic underlying lung disease or significant symptoms: insertion of intercostal drain (small drain by the Seldinger technique) In patients with recurrent pneumothorax or with a high risk of recurrent events and poor respiratory reserve, a pleurodesis can be performed. This can be medical (e.g., talc) or surgical (e.g., pleurectomy with VATS, pleural abrasion, sclerosing agent) 4 . Differential diagnosis Usually, the diagnosis is direct, but occasionally other entities should be considered: artifacts: air trapped between structures outside the chest skin fold: the apparent pleural edge is denser and can be seen extending beyond the thoracic cavity or appearing to fade blanket clothing monitoring leads (although these should be obvious) breast margin overlapping lung bubbles Giant bullous emphysema: differentiated from hypertensive pneumothorax by clinical stability, interstitial vascular marks projected with the bubbles and lack of hemithorax re-expansion after insertion of an intercostal catheter calcified pleural plaques another gas in abnormal sites pneumomediastinum pneumopericardium other causes of a hyperlucent hemithorax in the CT gas in the brachiocephalic vein cannulation iodinated contrast beam hardening artifact concentrated in a brachiocephalic vein.#info#"
                                 "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-11-50-34.png#bloquear_img#"
                                 "#con#Radiographic finding compatible with pneumothorax.#con#"
                                 "#webvideo#https://youtu.be/rVwYJOO2xXA#webvideo#")

        menu.Append(-1, "Pneumothorax | apicolateral",
                                 "#r#Visceral pleural border visible as a thin white line on the apicolateral surface of the " + nome_anat + ". A pneumothorax can be treated.#r#"
                                 "#info#There is a hydropneumothorax. Observe the air fluid level (blue arrow). The upper lobe is still attached to the chest wall by adhesions. This patient may have been treated for a previous pneumothorax. There is a pulmonary cyst in the upper lobe (red arrow). So, we can assume that the pneumothorax has something to do with a cystic lung disease. As this patient is a woman, lymphangioleiomyomatosis (LAM) is a possible diagnosis. LAM is a rare lung disease that results in a proliferation of smooth muscle in the lungs, resulting in the obstruction of small airways, leading to the formation of pulmonary cysts and pneumothorax. LAM also occurs in patients with tuberous sclerosis.#info#"
                                 "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-12-00-19.png#bloquear_img#"
                                 "#con#Radiographic finding compatible with pneumothorax.#con#"
                                 "#webvideo#https://youtu.be/7rNYjiRAImk#webvideo#")

        menu.Append(-1, "Hypertensive pneumothorax",
                                 "#r#There is an increase in intercostal spaces at " + nome_anat.split()[0] + " contralateral displacement of the mediastinum, depression of the hemidiaphragm and deep groove sign. The finding strongly suggests that it is a hypertensive pneumothorax.#r#"
                                 "#info#O reconhecimento de um pneumotórax depende do volume de ar no espaço pleural e da posição do corpo.  Numa radiografia em decúbito dorsal, um pneumotórax pode ser sutil e aproximadamente 30% dos pneumotórax não são detectados. Um sinal para procurar é o 'sinal do sulco profundo'.  Representa a lucência do ângulo costofrênico lateral que se estende em direção ao hipocôndrio (Figura). A imagem é de um paciente na UTI que está em ventilação mecânica. Houve uma exacerbação aguda da dispneia.  Há um sinal de sulco profundo à esquerda. Observe que o hemidiafragma esquerdo está deprimido.  Este é um achado importante, pois indica um pneumotórax hipertensivo.#info#"
                                 "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-12-07-53.png#bloquear_img#"
                                 "#con#Achado radiográfico compatível com pneumotórax hipertensivo.#con#"
                                 "#webvideo#https://youtu.be/G-_stz7zYck#webvideo#")

        menu = wx.Menu("Signs")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        submenu = wx.Menu("Westermark sign | Regional oligoemia")
        menu.Append(-1, submenu.GetTitle(), submenu)
        submenu.Append(-1, "Upper zone", "#r#Regional oligoemia is noted in the upper " + nome_anat + ", consistent with the Westermark sign, suggestive of pulmonary embolism.#r#"
                                                                                                              "#info#Westermark signal is a sign of pulmonary embolism seen on chest radiographs. It is one of the several signs described for pulmonary embolism on chest X-rays.#info#"
                                                                                                              "#con#Westermark sign, suggestive of pulmonary embolism.#con#"
                                                                                                              "#bloquear_img#screenshot-images.radiopaedia.org-2018.07.15-12-49-47.png#bloquear_img#"
                                                                                                              "#webvideo#https://youtu.be/sveVCO4-aiI#webvideo#")

        submenu.Append(-1, "Middle zone", "#r#Regional oligoemia is observed in the middle " + nome_anat + ", consistent with the Westermark sign, suggestive of pulmonary embolism.#r#"
                                                                                                        "#info#Westermark signal is a sign of pulmonary embolism seen on chest radiographs. It is one of the several signs described for pulmonary embolism on chest X-rays.#info#"
                                                                                                        "#con#Westermark sign, suggestive of pulmonary embolism.#con#"
                                                                                                        "#bloquear_img#screenshot-images.radiopaedia.org-2018.07.15-12-49-47.png#bloquear_img#"
                                                                                                        "#webvideo#https://youtu.be/OLWn8OoLpBE#webvideo#")

        submenu.Append(-1, "Lower zone", "#r#Regional oligoemia is noted in the lower " + nome_anat + ", consistent with the Westermark sign, suggestive of pulmonary embolism.#r#"
                                                                                                              "#info#Westermark signal is a sign of pulmonary embolism seen on chest radiographs. It is one of the several signs described for pulmonary embolism on chest X-rays.#info#"
                                                                                                              "#con#Westermark sign, suggestive of pulmonary embolism.#con#"
                                                                                                              "#bloquear_img#screenshot-images.radiopaedia.org-2018.07.15-12-49-47.png#bloquear_img#"
                                                                                                              "#webvideo#https://youtu.be/OLWn8OoLpBE#webvideo#")

        submenu.Append(-1, "Bell-shaped chest | Newborn", "#r#Low-volume lungs and a bell-shaped chest.#r#"
                                                                "#info#Respiratory distress syndrome (RDS) is a relatively common condition resulting from insufficient surfactant production that occurs in premature infants. In images, the condition usually appears as diffuse bilateral frosted glass lungs and relatively symmetrical with low volumes and a bell-shaped chest.#info#"
                                                                "#con#Finding may be related to prematurity.#con#"
                                                                "#bloquear_img#screenshot-radiopaedia.org-2018.07.15-12-18-28.png#bloquear_img#"
                                                                "#webvideo#https://youtu.be/gIK_WKbShyY#webvideo#")


        menu.AppendSeparator()
        menu.Append(-1, "Presence of Kerley B lines.", "#r#Presence of Kerley B lines.#r#"
                                                           "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Golden S Sign", "#r#Increased density in the medial and upper region of the right hemithorax with loss of volume and displacement of the trachea to the right, which may correspond to the hilar mass obstructing the bronchus of the right upper lobe resulting in partial collapse of the ipsilateral upper lobe.#r#"
                                                "#webvideo#https://youtu.be/SrzTPZBHk1w#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Butterfly Wing Sign", "#r#Bilateral alveolar opacities in the middle lung fields and parahilar region with symmetrical distribution and peripheral preservation, which seems to translate to alveolar edema, in the context of acute lung edema.#r#"
                                                     "#webvideo#https://youtu.be/7tRGFKcO-i8#webvideo#")

        self.menu_coracao.AppendSeparator()
        menu_pato = wx.Menu("Pathologies")
        self.menu_coracao.Append(-1, menu_pato.GetTitle(), menu_pato)
        menu_pato.Append(-1, "Primary tuberculosis", "#r#Homogeneous consolidation (without cavitation), in the lobes (upper or lower) of the " + nome_anat + ".#r#"
                                            "#webvideo#https://youtu.be/m8HpfLMSqCo#webvideo#")
        menu_pato.Append(-1, "Cavity Tuberculosis", "#r#A well-defined thick-walled cavitation lesion is observed in the right para-hilar area and at the base of the right lung, which may correspond to sequelae due to tuberculosis, and cannot exclude disease activity or inactivity by radiological criteria alone. Correlate the finding with clinical data, laboratory tests and past history.#r#"
                                            "#webvideo#https://youtu.be/m8HpfLMSqCo#webvideo#")


        menu_pato.AppendSeparator()
        menu_pato.Append(-1, "COPD | Signals", "#r#Pulmonary hyperinflation, bilateral hypertransparency, rectification of diaphragmatic hemicupulae, enlarged intercostal spaces, increased retrosternal air space and increased anteroposterior thoracic diameter, characterizing radiographic signs of COPD.#r#"
                                              "#webvideo#https://youtu.be/KUwFbDAHlJA#webvideo#")

        menu_pato.Append(-1, "Pulmonary hyperinflation, which must be compared with clinical data.", "#r#Pulmonary hyperinflation, which must be compared with clinical data.#r#"
                             "#webvideo#https://youtu.be/KUwFbDAHlJA#webvideo#")

        menu_pato.Append(-1, nome_anat.title() + " reduced in volume", "#r#" + nome_anat.title() + " reduced in volume.#r#"
                                                                                                    "#webvideo#https://youtu.be/5owzpKMKNH0#webvideo#")
        menu_pato.Append(-1, nome_anat + " reduced in volume | with peripheral veiling", "#r#" + nome_anat.title() + " reduced in volume with peripheral veiling.#r#"
                                                                                                                       "#webvideo#https://youtu.be/5owzpKMKNH0#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Atelectasis")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Atelectatic changes in the lung bases.", "#r#Atelectatic changes in the lung bases.#r#"
                                                                          "#webvideo#https://youtu.be/3_iggYB2A7k#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "To describe atelectasic",
                          "#r#Laminar atelectasis #desc_opa_pulmao_local# of the " + nome_anat + "#descrever_correlacionar#.#r#"
                          "#info#Atelectasia é colapso ou expansão incompleta do pulmão ou parte do pulmão. Este é um dos achados mais comuns em uma radiografia de tórax. É mais causada por uma lesão endobrônquica, como o tampão mucoso ou tumor. Também pode ser causado por compressão extrínseca centralmente por uma massa, como linfonodos ou compressão periférica por derrame pleural. Um tipo incomum de atelectasia é cicatricial e secundária a cicatrizes, tuberculose ou estado pós-radiação. A atelectasia está quase sempre associada a uma densidade linear aumentada na radiografia torácica. O ápice tende a estar no hilo. A densidade está associada à perda de volume. Alguns sinais indiretos de perda de volume incluem apinhamento vascular ou deslocamento fissural, traqueal ou mediastinal, em direção ao colapso. Pode haver hiperinsuflação compensatória dos lobos adjacentes, ou elevação hilar (colapso do lobo superior) ou depressão (colapso do lobo inferior). O colapso segmentar e subsegmentar pode mostrar opacidades lineares, curvilíneas em forma de cunha. Isso é mais frequentemente associado com pacientes pós-operatórios e aqueles com hepatoesplenomegalia maciça ou ascite.#info#"
                          "#bloquear_img#screenshot-www.med-ed.virginia.edu-2018.06.06-11-06-58.png#bloquear_img#"
                          "#con#Atelectatic lobe of the " + nome_anat + "#con#"
                          "#webvideo#https://youtu.be/qms-_ob9Fgs#webvideo#")

        menu.AppendSeparator()
        menu.Append(-1, "Atelectatic streaks in the lung bases.",
                                                  "#r#Atelectatic streaks in the lung bases.#r#"
                                                  "#info#Atelectasis is collapse or incomplete expansion of the lung or part of the lung. This is one of the most common findings on a chest X-ray. It is most often caused by an endobronchial lesion, such as the mucous plug or tumor. It can also be caused by extrinsic compression centrally by a mass, such as lymph nodes or peripheral compression by pleural effusion. An unusual type of atelectasis is scarring and secondary to scarring, tuberculosis or a post-radiation state. Atelectasis is almost always associated with increased linear density on chest radiography. The apex tends to be in the hilum. Density is associated with loss of volume. Some indirect signs of loss of volume include vascular crowding or fissural, tracheal or mediastinal displacement, towards collapse. There may be compensatory hyperinflation of the adjacent lobes, or hilar elevation (collapse of the upper lobe) or depression (collapse of the lower lobe). Segmental and subsegmental collapse can show linear, curvilinear wedge-shaped opacities. This is most often associated with postoperative patients and those with massive hepatosplenomegaly or ascites.#info#"
                                                  "#bloquear_img#screenshot-www.med-ed.virginia.edu-2018.06.06-11-06-58.png#bloquear_img#"
                                                  "#con#Atelectatic streaks in the lung bases.#con#"
                                                  "#webvideo#https://youtu.be/3_iggYB2A7k#webvideo#")


        self.menu_coracao.AppendSeparator()
        menu = wx.Menu("Medical supplies")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Hemithorax drain", "#r#Drain in the hemithorax " + nome_anat.split()[0] + " #descrever_trageto_do_tubo# #descrever_local_extremidade_do_tubo#.#r#"
                                             "#webvideo#https://youtu.be/qR3VcueqBgc#webvideo#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat

    def traqueia(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="trachea"):
        """Return customized button. must define
        the position by x and y."""

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0] + nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0]+ nome_anat[1:])
        self.menu_coracao.Append(-1, "Trachea centered on the mediastinum.", "#r#Trachea centered on the mediastinum.#r#"
                                                                         "#webvideo#https://youtu.be/tqZW3u-by5s#webvideo#")
        menu = wx.Menu("Deviated trachea")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Trachea deflected to the right.", "#r#Trachea deflected to the right.#r#"
                                                           "#webvideo#https://youtu.be/tqZW3u-by5s#webvideo#")
        menu.Append(-1, "Trachea deflected to the left.", "#r#Trachea deflected to the left.#r#"
                                                            "#webvideo#https://youtu.be/tqZW3u-by5s#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Tracheostomy tube in typical position.", "#r#Tracheostomy tube in typical position.#r#"
                                                                                 "#webvideo#https://youtu.be/Z-eJIe4G4jI#webvideo#")
        self.menu_coracao.Append(-1, "Endotracheal tube", "#r#Presence of endotracheal tube.#r#"
                                                          "#webvideo#https://youtu.be/2WHN42WzGJg#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Subcarinal lymphadenopathy", "#r#There is a displacement of the esophageal heartburn, opacity causing mediastinal enlargement and an increase in the subcarinal angle, which may correspond to subcarinal lymphadenopathy.#r#"
                                                                  "#info#Another common cause of displacement of the azioesophageal line is subcarinal lymphadenopathy. Note the displacement of the upper part of the azigoesophageal line on the chest X-ray in the area below the carina. This is the result of massive lymphadenopathy in the subcarinal region (station 7). There are also knots on the right side of the trachea, displacing the right paratracheal line. In PET we can appreciate massive lymphadenopathy much better than in chest radiography. There are also lymphomas in the neck. This is an important finding, since these nodes are accessible for biopsy. Continue with CT and ultrasound images.#info#"
                                                                  "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-10-54-29.png#bloquear_img#"
                                                                  "#con#Finding causing mediastinal enlargement and increased subcarinal angle, which may correspond to subcarinal lymphadenopathy.#con#"
                                                                  "#webvideo#https://youtu.be/HZlOWgurwe8#webvideo#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat

    def esofago(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="esophagus"):
        """Return customized button. must define
        the position by x and y."""

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0] + nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0]+ nome_anat[1:])
        self.menu_coracao.Append(-1, "Normal esophagus.", """#r#Normal esophagus.#r#
#info#The azigoesophageal recess is the region below the level of the azygous vein arch in which the right lung forms an interface with the mediastinum between the heart anteriorly and the spine posteriorly. It is bordered on the left by the esophagus. The deviation of the azygosesophageal line is caused by: 1. Hiatal hernia 2. Left atrial enlargement 3. Esophageal disease 4. Subcarinal lymphadenopathy 5. Bronchogenic cyst Conclusion suggestion: Esophagus of typical appearance.#info#
#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.02-20-30-33.png#bloquear_img#
#con#Esophagus of usual appearance.#con#
#webvideo#https://youtu.be/cNAr4BXEaOw#webvideo#""")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Hiatus hernia", "#r#Retrocardiac opacity with hydroaero level, corresponding to hiatus hernia.#r#"
                                                        "#info#Hiatal hernia Dr. Henry Knipe and R Bronson et al. Hiatal hernias occur when there is herniation of the abdominal contents through the esophageal hiatus from the diaphragm to the chest cavity. Epidemiology The prevalence of hiatus hernia increases with age, with a slight female predilection. Clinical presentation Many patients with hiatus hernia are asymptomatic and it is an incidental finding. However, symptoms may include epigastric or chest pain, postprandial fullness, nausea and vomiting 3. Sometimes hiatus hernias are considered synonymous with gastro-oesophageal reflux disease (GERD), but there is a weak correlation between the two conditions. Pathology The most common content of a hiatal hernia is the stomach. There are two main types of hiatal hernia (although they can coexist): sliding hiatal hernia (> 90%) rolling hiatal hernia (paraesophageal) (<10%) Some divide them into four types: type 1: sliding hiatal hernia ( ~ 95%) type 2: paraesophageal hiatal hernia with gastroesophageal junction in normal position type 3: mixed or compound type, paraesophageal hiatal hernia with displaced gastroesophageal junction type 4: mixed or compound hiatal hernia with additional viscera hernia Subtypes Hernia of sliding hiatus This is the most common type of hiatal hernia (~ 90%). The gastroesophageal junction (GOJ) is usually displaced> 2 cm above the esophageal hiatus. The esophageal hiatus is often abnormally enlarged to 3-4 cm (the upper limit of normal is 1.5 cm). The gastric fundus can also be displaced above the diaphragm and present itself as a retrocardiac mass on a chest X-ray. The presence of an air fluid level in the mass suggests the diagnosis. Small sliding hiatus hernias usually decrease in an upright position. The mere presence of a sliding hiatus hernia is of limited clinical significance in most cases. The function of the lower esophageal sphincter and the presence of pathological gastroesophageal reflux are crucial factors to produce symptoms and cause complications. Rolling (para-oesophageal) hiatus hernia Rolling (para-oesophageal) hernia is much less common than the type of sliding. The GOJ remains in its normal location while a part of the stomach hernia above the diaphragm. Mixed rolling and sliding hiatal hernia Mixed or composite hiatal hernia is the most common type of paraesophageal hernia. The GOJ is displaced to the chest with a large portion of the stomach, which is usually abnormally rotated. Radiographic characteristics Radiography simple retrocardiac opacity with hydroaero level Fluoroscopy numerous thick gastric folds within the suprahiatal sac tortuous esophagus with a gastroesophageal junction eccentric CT focal fat collection in the middle mediastinum the hernia omentum through the phrenic-esophageal ligament may see an increase in fat around the distal esophagus para-esophageal hernia through an enlarged esophageal hiatus view contents, size, orientation of the stomach hernia inside the lower thorax herniated content is adjacent to the esophageal enlargement of the esophageal hiatus diaphragmatic cracks (> 15 mm): increase the distance between the crura and the esophageal wall Treatment and prognosis Symptomatic hiatological hernias, especially types 2-4, should be treated surgically 5. Complications Hiatal hernia containing the stomach can result in a gastric volvulus, which in turn presents itself as intestinal obstruction and can result in ischemia / infarction, or very rarely a tension gastrothorax, causing respiratory failure and eventual cardiac arrest. Differential diagnosis On a frontal chest radiography, consider: retrocardiac lung abscess retrocardiac empyema esophageal epiphrenic diverticulum (pulse) phrenic ampoule postoperative change: esophagectomy with gastric pull-up procedure In the scenario of trauma, consider diaphragmatic rupture. https://radiopaedia.org/articles/hiatus-hernia#info#"
                                                        "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-10-35-27.png#bloquear_img#"
                                                        "#con#Retrocardiac opacity with hydroaero level, corresponding to hiatus hernia.#con#"
                                                        "#webvideo#https://youtu.be/FoRZNR_qBb0#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Esophagogastric tube.", "#r#Esophagogastric tube.#r#")
        self.menu_coracao.Append(-1, "Digestive tube with distal end not visible.", "#r#Digestive tube with distal end not visible.#r#")
        self.menu_coracao.AppendSeparator()

        self.menu_coracao.Append(-1, "Achalasia | Megaesophagus", "#r#The esophagus is enlarged with residual fluid and displacement of the azo-esophageal line both superiorly and inferiorly. Finding may correspond to achalasia.#r#"
                                                        "#info#Achalasia: Dr. Arjun Shivananda and A.Prof Frank Gaillard et al. Achalasia (primary achalasia) is a failure of organized esophageal peristalsis, which causes decreased relaxation of the lower esophageal sphincter, resulting in food stasis and, often, in marked dilation of the esophagus. Obstruction of the distal esophagus from other non-functional etiologies, notably malignancy, may have a similar presentation and may have been called secondary achalasia or pseudoachalasia. Epidemiology Primary achalasia is most commonly seen in middle and late adulthood (age between 30 and 70 years), with no predilection for sex 6. Most cases are idiopathic; however, a similar appearance can occur in Chagas' disease. Authors differ in terms of reserving the term achalasia for idiopathic cases or to include Chagas' disease. Clinical presentation Patients usually experience dysphagia for solids and liquids: this is in contrast to dysphagia for solids only in cases of esophageal carcinoma 7 pain / discomfort in the chest eventual regurgitation Symptoms are initially intermittent. Patients may also experience complications from long-standing achalasia: esophageal carcinoma the most feared complication, seen in approximately 5%, most often in the middle of the esophagus thought to occur because of chronic mucosal irritation by food stasis and pneumonia secretions by aspiration: the chronic presence of liquid debris in the esophagus makes patients very prone to aspiration esophagitis due to acute acute airway obstruction: it is a rare complication that requires immediate esophageal decompression with nasogastric tube Pathology Peristalsis in the distal segment of the esophageal smooth muscle it may be lost due to an abnormality of the Auerbach plexus (responsible for smooth muscle relaxation), resulting in weak and uncoordinated contractions that are not propulsive. The abnormality can also occur in the vagus nerve or in its dorsal motor nucleus. The lower esophageal sphincter does not eventually relax, partially or completely, with high pressures demonstrated by manometry 4. At the beginning of the course of achalasia, the tone of the lower esophageal sphincter may be normal or the changes may be subtle. Radiographic characteristics Achalasia characteristically involves a short segment (less than 3.5 cm in length) of the distal esophagus. Simple radiography Chest radiography findings include: convex opacity that overlaps the right mediastinum. occasionally it may present as a left convex opacity if the thoracic aorta is tortuous level of air fluid due to stasis in a thoracic esophagus full of retained secretions and small gastric bubble food or absent anterior displacement and arching of the trachea in the lateral view may be seen irregular alveolar opacities, usually bilateral. These represent acute pneumonitis or chronic aspiration pneumonia related to dysphagia Fluoroscopy with barium swallow A study of barium swallowing can be used to confirm dilation of the esophagus, in addition to assessing mucosal abnormalities. Findings include: bird beak signal esophageal dilation tramway appearance: central longitudinal lucidity limited by barium on both sides 8 incomplete relaxation of the lower esophageal sphincter that is not coordinated with pool esophageal contraction or barium stasis in the esophagus when the esophagus became atonic or non-contractile (a late feature of the disease) uncoordinated, non-propulsive and tertiary contractions (see case 1) failure of normal peristalsis to clear the barium esophagus when the patient is in decubitus, with no primary waves identified when the barium spine is high enough (with the patient standing), the hydrostatic pressure can overcome the pressure of the lower esophageal sphincter, allowing the passage of esophageal contents a hot or carbonated drink during the exam can help to visualize sphincter relaxation and emptying of barium CT Patients with uncomplicated achalasia demonstrate dilated, thin-walled esophagus s, filled with liquid / food scraps. In general, CT has little role in the direct evaluation of patients with achalasia, but it is useful in the evaluation of common complications. Careful assessment of the esophageal wall should be performed to identify any focal thickening regions that may indicate malignancy. The lungs should be inspected for evidence of aspiration.#info#"
                                                        "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-11-09-38.png#bloquear_img#"
                                                 "#con#Radiographic finding raises the diagnostic hypothesis of achalasia, according to clinical criteria, investigation with contrasted radiographic examination of the esophagus is suggested.#con#"
                                                 "#webvideo#https://youtu.be/kIQ3FVbsCxc#webvideo#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


    def subclavia(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="subclavian"):
        """Return customized button. must define
        the position by x and y."""

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0] + nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0]+ nome_anat[1:])
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Normal subclavian", "#r#Normal subclavian.#r#"
                                                         "#webvideo#https://youtu.be/tqZW3u-by5s#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, nome_anat.title() + "catheter is noted.", "#r#" + nome_anat + " catheter is noted.#r#")
        self.menu_coracao.AppendSeparator()
        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


    def material_extra(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="medical stuff", gen="o"):
        """Return customized button. must define
        the position by x and y."""

        #nome_anat_ex_direito = nome_anat.split()[-1].replace("right", "right").replace("left", "left")
        #nome_anat_ex_direita = nome_anat.split()[-1].replace("right", "right").replace("left", "left")

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0] + nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])

        if "right hypochondrium" in nome_anat:
            self.menu_coracao.Append(-1, "Cholecystectomy surgical clips", "#r#Two linear radiopaque images projected on the " + nome_anat + " are observed, which may correspond to cholecystectomy surgical clips.#r#")

        if "right iliac fossa" in nome_anat:
            self.menu_coracao.Append(-1, "Clipes cirúrgicos de apendicectomia", "#r#There are two linear radiopaque images projected on the " + nome_anat + ", which may correspond to appendectomy surgical clips.#r#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat



    def diafragma(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="diafragma"):
        """Return customized button. must define
        the position by x and y."""

        nome_anat_ex_direita = nome_anat.split()[1].replace("right", "right").replace("left", "left")
        nome_anat_ex_direito = nome_anat.split()[1]

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0]+ nome_anat[1:])

        menu = wx.Menu("Morphology")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Normal", "#r#Diaphragmatic hemicupulas in their usual positions and without changes suggestive of underlying pathologies.#r#"
                                  "#webvideo#https://youtu.be/AFZtL9OCiIs#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Hemicome rectification", "#r#" + nome_anat + " diaphragmatic rectification.#r#"
                         "#webvideo#https://youtu.be/KUwFbDAHlJA#webvideo#")

        menu.Append(-1, "Flattening of the diaphragm", "#r#Flattening of the diaphragm#r#"
                                                    "#webvideo#https://youtu.be/KUwFbDAHlJA#webvideo#")

        self.menu_coracao.AppendSeparator()
        menu = wx.Menu("Elevation diaphragm")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Elevated " + nome_anat.split()[0] + ".", "#r#Elevated " + nome_anat.split()[0] + " diaphragmatic hemicupula.#r#"
                                                                                                "#webvideo#https://youtu.be/df9gvTl0P18#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Discreet elevation due to probable gas distension in the splenic flexure.", "#r#Discrete elevation of the " + nome_anat.split()[0] + " diaphragmatic hemicupula, due to probable gas distension in the splenic flexure.#r#"
                                                                                                 "#info#Pericardial cyst? Pericardial cysts are connected to the pericardium and usually contain clear fluid. Most pericardial cysts appear at the anterior cardiophrenic angle, most frequently on the right, but can be seen as high as the pericardial recesses at the level of the proximal aorta and pulmonary arteries. Most patients are asymptomatic. On chest radiography, it appears that there is an elevated left hemidiaphragm. On CT, however, there is a cyst connected to the pericardium.#info#"
                                                                                                 "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-09-18-43.png#bloquear_img#"
                                                                                                 "#webvideo#https://youtu.be/df9gvTl0P18#webvideo#")

        menu.Append(-1, "Discrete elevation of the " + nome_anat.split()[0] + " diaphragmatic hemicupula, due to probable gas distension of the gastric bubble.", "#r#Discrete elevation of the " + nome_anat.split()[0] + " diaphragmatic hemicupula, due to probable gas distension of the gastric bubble.#r#"
                                                                                                                                                        "#webvideo#https://youtu.be/df9gvTl0P18#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, nome_anat + " eventration.", "#r#" + nome_anat +" eventration.#r#"
                                                            "#webvideo#https://youtu.be/PXNotbYirh0#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Free intra-abdominal gas")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Free gas under the " + nome_anat + ", according to recent abdominal surgery.", "#r#Free gas under the " + nome_anat + ", according to recent abdominal surgery.#r#"
                                                                                                        "#webvideo#https://youtu.be/VfL7qKk25o0#webvideo#")

        menu.AppendSeparator()
        menu.Append(-1, "under the " + nome_anat + " | pneumoperitoneum.", "#r#Free intra-abdominal gas under the " + nome_anat + ", compatible with pneumoperitoneum.#r#"
                                                                                                                                                                                            "#webvideo#https://youtu.be/VfL7qKk25o0#webvideo#")
        menu.Append(-1, "under the diaphragm | pneumoperitoneum.", "#r#Free intra-abdominal gas under the diaphragm, compatible with pneumoperitoneum.#r#"
                                                              "#webvideo#https://youtu.be/7QY3OvRzFlQ#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Consolidation")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Consolidation | loss of silhouette", "#r#The " + nome_anat + " is obscured by the consolidation process.#r#"
                                                              "#info#Consolidation of the right middle lobe The right edge of the heart (edge of the right atrium) is obscured Consolidation (asterisk) is limited above by a sharp line, formed by the horizontal fissure The pathology must therefore involve the right middle lobe More extensive shading as well involves the right and left perihilar regions Clinical information Child with cough and fever Diagnosis Pneumonia involving the right middle lobe.#info#"
                                                              "#con#Pulmonary consolidation.#con#"
                                                              "#bloquear_img#screenshot-www.radiologymasterclass.co.uk-2018.07.21-21-52-44.png#bloquear_img#"
                                                              "#webvideo#https://youtu.be/fW14iNSapw0#webvideo#")


        menu = wx.Menu("Pathologies")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "COPD","#r#Pulmonary hyperinflation, rectification of diaphragmatic hemicupulas and increased retrosternal air space, featuring radiographic signs of COPD. Correlate with clinical data.#r#"
                               "#webvideo#https://youtu.be/KUwFbDAHlJA#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Bochdalek hernia", "#r#There is soft tissue opacity in the " + nome_anat.split()[0] + " lung base seen in the postero-basal region on the lateral radiography. Finding compatible with Bochdalek's hernia diagnostic hypothesis.#r#"
                                                            "#info#Bochdalek's hernia is characterized by a defect in the closure of the pleuroperitoneal canal during the embryological development of the diaphragm, between the 8th and 10th week of life. It is the result of the incomplete fusion of the lumbar (posterior) and costal (lateral) elements during the development of the diaphragm. The consequence is the protrusion of the abdominal viscera through the diaphragm into the chest cavity. Its diagnosis is more frequent in children (90% in the neonatal period) and rare in adults (10%), being located more commonly in the left hemithorax. Contrast radiological examination and computed axial tomography confirm the diagnosis. Although in the literature we find a greater tendency to indicate surgical treatment, it is important to point out that, with an individual assessment, it is possible to select individuals that are amenable to conservative clinical management, thus avoiding an exposure to the surgical risks of patients with little symptoms and quality. of life unchanged.#info#"
                                                            "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-16-11-15.png#bloquear_img#"
                                                            "#con#A finding compatible with Bochdalek's hernia in the region of the " + nome_anat.split()[0] + "diaphragmatic hemicupula, the clinical criterion suggests requesting a computed tomography scan of the chest and abdomen to confirm the diagnosis.#con#"
                                                                                                                                                                                                                                           "#webvideo#https://youtu.be/XmxjJSuVnLk#webvideo#")

        menu.Append(-1, "Diaphragmatic hernia or phrenic dome elevation?", "#r#Gastric needle and intestinal loop of the topography of the splenic flexure distended by gaseous content and displaced cranially, projected #desc_opa_pulmao_local# of the right hemithorax, which may represent diaphragmatic hernia or elevation of the phrenic dome, it is suggested at clinical criteria to proceed with the investigation with chest tomography.#r#"
                                                                                                                                                                                                                                                                                             "#bloquear_img#img_sis_hernia_diafragmatica_frenica.png#bloquear_img#"
                                                                                                                                                                                                                                                                                             "#info#Diaphragmatic hernia Dr. Henry Knipe and A.Prof Frank Gaillard et al. Diaphragmatic hernias are defined as congenital or acquired defects in the diaphragm. Demography and Congenital aetiology There are two main types of congenital diaphragmatic hernia (HDC), which are uncommon but distinct entities that usually occur on the left side (80%) of the diaphragm 1,2: Bochdalek hernia: most common (95%) , located posterolaterally and usually present in childhood 2 Morgagni hernia: smaller, anterior and presents later, through sternocostal angles 2 Acquired There are a variety of etiologies for acquired diaphragmatic hernias that usually occur in adulthood 1: traumatic diaphragmatic rupture through penetrating injury (65%) or blunt trauma (35%) 3 iatrogenic hiatus hernia Depending on the location and size of the defect, retroperitoneal or intra-abdominal organs and tissues may be prolapsed to the chest cavity due to intra negative pressure -torácica 1 \ n \ n https://radiopaedia.org/articles/diaphragmatic-hernia#info#"
                                                                                                                                                                                                                                                                                             "#webvideo#https://youtu.be/FoRZNR_qBb0#webvideo#")

        menu.AppendSeparator()
        menu.Append(-1, "Chilaiditi sign", "#r#Radiography reveals air in the right hepatodiaphragmatic space and radiopaque folds interposed by layers suggest that the gas is inside intestinal loops and not free, and may be a hollow viscera ('Chilaiditi sign'). #descrever_correlacionar##r#"
                                               "#info#Chilaiditi's sign (pseudopneumoperitoneum) Dr. Daniel J Sino and Dr. Vikas Shah et al. Chilaiditi's sign refers to the interposition of the intestine, usually colon, between the lower surface of the right hemidiaphragm and the upper surface of the liver. It can be misinterpreted as a true pneumoperitoneum, resulting in unnecessary additional investigations and/or therapy. The presence of pain associated with and attributed to the sign is called Chilaiditi syndrome. Radiographic features Simple radiography Features that suggest Chilaiditi's sign include: gas between the liver and the rough diaphragm bends inside the gas, suggesting that it is inside the intestine and not free CT If there is clinical suspicion of abdominal visceral perforation and simple radiographic appearances are not clear, abdominal CT may be performed to clarify if there is pneumoperitoneum. CT can clearly demonstrate the presence of interposed colonic loops between the right hemidiaphragm and the liver, without free intraperitoneal air.  Treatment and prognosis Asymptomatic patients with Chilaiditi's sign do not need additional images or treatment. History and etymology He is named after Demetrius Chilaiditi (1883-1975) 1 , a Greek radiologist who described the radiographic findings in 1910 3 while working in Vienna, Austria. Although the first description of colon interposition between liver and right hemidiaphragm was published by Cantini in 1865.https://radiopaedia.org/articles/chilaiditi-sign-pseudopneumoperitoneum#info#"
                                               "#bloquear_img#screenshot-upload.wikimedia.org-2018.08.24-09-39-34.png#bloquear_img#"
                                               "#con#Radiografia revela ar no espaço hepatodiafragmático direito, sugerindo tratar-se de víscera oca (sinal de Chilaiditi).#con#"
                                               "#webvideo#https://youtu.be/DIVpuzKwTaU#webvideo#")

        self.menu_coracao.AppendSeparator()

        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Atelectatic streaks in the lung bases.", "#r#Atelectatic streaks in the lung bases.#r#"
                                                                                    "#webvideo#https://youtu.be/3_iggYB2A7k#webvideo#")
        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


# stop 11/12/2020
# start 11/13/2020


    def costodiaphragmatic_recess(self, x=1, y=1, largura=1, altura=1, nome_anat ="costodiaphragmatic recess"):
        """Return customized button. must define
        the position by x and y."""

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])

        menu = wx.Menu("Costodiaphragmatic recess normal")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)

        menu.Append(-1, nome_anat.title()[0] + nome_anat[1:] + " normal.")
        menu.AppendSeparator()
        menu.Append(-1, "Costodiaphragmatic recess normal.",
                                                  "#r#Costodiaphragmatic recess normal.#r#"
                                                  "#info#The pleural fluid can become encysted. Here we see fluid trapped inside the fissure. This can sometimes give the impression of a mass and is called a 'disappearance tumor'.#info#"
                                                  "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-11-41-54.png#bloquear_img#"
                                                  "#con#Costodiaphragmatic recess normal.#con#"
                                                  "#webvideo#https://youtu.be/AFZtL9OCiIs#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Impaired evaluation")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, nome_anat.title()[0] + nome_anat[1:] + " with impaired evaluation.")
        menu.AppendSeparator()
        menu.Append(-1, "Costodiaphragmatic recess with impaired evaluation.", "#r#Costodiaphragmatic recess with impaired evaluation.#r#"
                                                                          "#webvideo#https://youtu.be/AFZtL9OCiIs#webvideo#")
        menu.AppendSeparator()

        submenu1 = wx.Menu("Outside of radiography")
        menu.Append(-1, submenu1.GetTitle(), submenu1)
        submenu1.Append(-1, "Costodiaphragmatic recess outside of radiography", "#r#Costodiaphragmatic recess outside of radiography.#r#"
                                                      "#con#Costodiaphragmatic recess outside of radiography.#con#"
                                                                  "#webvideo#https://youtu.be/AFZtL9OCiIs#webvideo#")
        submenu1.AppendSeparator()
        submenu1.Append(-1, nome_anat[0].title() + nome_anat[1:] + " outside of radiography", "#r#" + nome_anat[0].title() + nome_anat[1:] + " outside of radiography." + "#r#"
                                                      "#con#" + nome_anat[0].title() + nome_anat[1:] + " outside of radiography." + "#con#"
                                                                                                                           "#webvideo#https://youtu.be/AFZtL9OCiIs#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Opacification")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Location | Optophrenic  " + nome_anat,
                                                  "#r#Opacification on " + nome_anat + "#descrever_grau_derrame_pleural_ex_pequeno_singular_masculino#.#r#"
                                                  "#info#A tabela lista as causas mais comuns de opacidade pleural.#info#"
                                                  "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-12-11-28.png#bloquear_img#"
                                                  "#con#recesso costofrênicos obliterados, sugerindo derrame pleural bilateral.#con#"
                                                  "#webvideo#https://youtu.be/ra8aIosCEe4#webvideo#")

        menu.AppendSeparator()
        menu.Append(-1, "Bilateral | Obliteration of costophrenic recesses",
                                                  "#r#Obliteração dos recesso costofrênicos #descrever_grau_derrame_pleural_bilateral_ex_pequeno_masculino#.#r#"
                                                  "#info#A tabela lista as causas mais comuns de opacidade pleural.#info#"
                                                  "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-12-11-28.png#bloquear_img#"
                                                  "#con#recesso costofrênicos obliterados, sugerindo derrame pleural bilateral.#con#"
                                                  "#webvideo#https://youtu.be/CVimots4lGA#webvideo#")

        menu.AppendSeparator()
        if "costophrenic recess" in nome_anat:
            self.menu_coracao.AppendSeparator()
            menu.Append(-1, "Pseudo-diaphragmatic shadow of the costophrenic angle " + nome_anat.replace("seio costofrênico direito", "direito").replace("seio costofrênico esquerdo", "esquerdo"), "#r#Pseudo-diaphragmatic shadow of the costophrenic angle " + nome_anat.replace("seio costofrênico direito", "direito").replace("seio costofrênico esquerdo", "esquerdo") + ", finding associated with the patient's rotation when the radiography was obtained, and should not be interpreted as a pathological finding until a new chest radiography with an appropriate technique is obtained.#r#"
                                                                                                                                                                                                                                                                                                                                                        "#webvideo#https://youtu.be/4WvsSwAIR2w#webvideo#")
        self.menu_coracao.Append(-1, "Deep sulcus sign", "#r#Deep sulcus sign in " + nome_anat + ". May be hypertensive pneumothorax.#r#"
                                                                                                               "#webvideo#https://youtu.be/4WvsSwAIR2w#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Consolidation")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Consolidation | loss of silhouette", "#r#" + nome_anat + " it is obscured by the consolidation process.#r#"
                                                              "#info#Consolidation of the right middle lobe The right edge of the heart (edge of the right atrium) is obscured The consolidation (asterisk) is limited above by a sharp line, formed by the horizontal fissure The pathology must therefore involve the right middle lobe More extensive shading also involves the right and left peri-hilar regions Clinical information Child with cough and fever Diagnosis Pneumonia involving the right middle lobe.#info#"
                                                              "#con#Pulmonary consolidation.#con#"
                                                              "#bloquear_img#screenshot-www.radiologymasterclass.co.uk-2018.07.21-21-52-44.png#bloquear_img#"
                                                                                  "#webvideo#https://youtu.be/qms-_ob9Fgs#webvideo#")

        if "right" in nome_anat:
            menu = wx.Menu("Transparency of the " + nome_anat)
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Hypotransparency of " + nome_anat + " | Chilaiditi sign", "#r#Hypotransparency of " + nome_anat + " suggests air in the diaphragmatic hepatic space, which may be hollow viscera ('Chilaiditi sign'). #descrever_correlacionar##r#"
                                                   "#info#Sinal de Chilaiditi (pseudopneumoperitoneum) Dr. Daniel J Sino e Dr. Vikas Shah et al. Sinal de Chilaiditi refere-se à interposição do intestino, geralmente cólon, entre a superfície inferior do hemidiafragma direito e a superfície superior do fígado. Pode ser mal interpretado como um verdadeiro pneumoperitônio, resultando em investigações adicionais desnecessárias e / ou terapia. A presença de dor associada e atribuída ao sinal é denominada síndrome de Chilaiditi . Características radiográficas Radiografia simples Recursos que sugerem sinal de Chilaiditi incluem: gás entre o fígado e o diafragma rugal dobra dentro do gás, sugerindo que ele está dentro do intestino e não está livre CT Se houver suspeita clínica de perfuração visceral abdominal e aparências radiográficas simples não estiverem claras, a TC abdominal pode ser realizada para esclarecer se há pneumoperitônio. A TC pode demonstrar claramente a presença de alças colônicas interpostas entre o hemidiafragma direito e o fígado, sem ar intraperitoneal livre.  Tratamento e prognóstico Pacientes assintomáticos com sinal de Chilaiditi não necessitam de imagens adicionais ou tratamento. História e etimologia É nomeado após  Demetrius Chilaiditi (1883-1975) 1 ,  radiologista grego que descreveu as descobertas radiográficas em 1910 3 enquanto trabalhava em Viena, na Áustria. Embora a primeira descrição de interposição de cólon entre o fígado e o hemidiafragma direito tenha sido publicada por Cantini em 1865.\n\nhttps://radiopaedia.org/articles/chilaiditi-sign-pseudopneumoperitoneum#info#"
                                                   "#bloquear_img#screenshot-upload.wikimedia.org-2018.08.24-09-39-34.png#bloquear_img#"
                                                   "#con#Radiography reveals air in the right hepatodiaphragmatic space, suggesting it is hollow viscera (Chilaiditi sign).#con#"
                                                   "#webvideo#https://youtu.be/5WKLjAisvsc#webvideo#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat

    def mediastino(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="mediastinum"):
        """Return customized button. must define
        the position by x and y."""

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0]+ nome_anat[1:])

        menu = wx.Menu("Normal")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Mediastinum without particularities.", "#r#Mediastinum without particularities.#r#"
                                                            "#webvideo#https://youtu.be/ywR4b5JhT-Q#webvideo#")
        menu.Append(-1, "Mediastinum centered and without particularities.", "#r#Mediastinum centered and without particularities.#r#"
                                                                       "#webvideo#https://youtu.be/ywR4b5JhT-Q#webvideo#")

        menu.Append(-1, "Mediastinum centered and without enlargement.", "#r#Mediastinum centered and without enlargement.#r#"
                                                                              "#info#The mediastinum can be divided into an anterior, middle and posterior compartment, each with its own pathology.#info#"
                                                                              "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-09-58-32.png#bloquear_img#"
                                                                              "#con#Radiography without pathological mediastinal changes.#con#"
                                                                  "#webvideo#https://youtu.be/ywR4b5JhT-Q#webvideo#")

        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Mediastinal enlargement.", "#r#Mediastinal enlargement.#r#"
                                                          "#info#In the PA view, the upper mediastinum is enlarged. The lateral view is useful in this case because it shows a density in the retrosternal space. The differential diagnosis is now limited to a mass in the anterior mediastinum (4 T's) This was Hodgkin's lymphoma.#info#"
                                                        "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-15-04-02.png#bloquear_img#"
                                                                 "#webvideo#https://youtu.be/ywR4b5JhT-Q#webvideo#")

        self.menu_coracao.Append(-1, "Mediastinal enlargement, probably of vascular origin.", "#r#Mediastinal enlargement, probably of vascular origin.#r#"
                                                                                              "#webvideo#https://youtu.be/mEGTzW6k2ww#webvideo#")

        self.menu_coracao.Append(-1, "Subcarinal lymphadenopathy",
                                 "#r#There is a displacement of the esophageal heartburn, opacity causing mediastinal enlargement and an increase in the subcarinal angle, which may correspond to subcarinal lymphadenopathy.#r#"
                                 "#info#Another common cause of displacement of the azioesophageal line is subcarinal lymphadenopathy. Note the displacement of the upper part of the azigoesophageal line on the chest X-ray in the area below the carina. This is the result of massive lymphadenopathy in the subcarinal region (station 7). There are also knots on the right side of the trachea, displacing the right paratracheal line. In PET we can appreciate massive lymphadenopathy much better than in chest radiography. There are also lymphomas in the neck. This is an important finding, since these nodes are accessible for biopsy. Continue with CT and ultrasound images.#info#"
                                 "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-10-54-29.png#bloquear_img#"
                                 "#con#Find causing mediastinal enlargement and subcarinal angle increase may correspond to subcarinal lymphadenopathy.#con#")


        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "COPD signs", "#r#Increase in retrosternal air space, associated with lowering of phrenic domes, which may be related to some degree of COPD. Correlate to clinical data.#r#"
                                                   "#webvideo#https://youtu.be/KUwFbDAHlJA#webvideo#")
        self.plt_btn_anat.SetMenu(self.menu_coracao)
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Pneumomediastinum", "#r#Translucent radio strips crisscrossed over the mediastinum that extends to the neck.#r#"
                                                     "#info#Pneumomediastinum: Findings for pneumomediastinum include; lucidities intertwined over the mediastinum that extend to the neck and elevation of the parietal pleura along the mediastinal borders. Causes of pneumomediastinum include; asthma, surgery (postoperative complication), traumatic tracheobronchial rupture, abrupt changes in intrathoracic pressure (vomiting, coughing, exercise, childbirth), rupture of the esophagus, barotrauma and crack consumption. Pneumomediastinum should be distinguished from pneumopericardium and pneumothorax. In the pneumopericardium, air may be present under the heart, but it does not enter the neck.#info#"
                                                     "#bloquear_img#screenshot-www.med-ed.virginia.edu-2018.06.06-16-44-41.png#bloquear_img#"
                                                     "#con#Pneumomediastinum.#con#"
                                                     "#webvideo#https://youtu.be/G-_stz7zYck#webvideo#")



        menu = wx.Menu("Mediastinal lines")
        menu.Append(-1, "Paratracheal online alteration", "#r#Alteration in the paratracheal line.#r#"
                                                              "#info#Mediastinal lines: Mediastinal lines or stripes are interfaces between the soft tissue of mediastinal structures and the lung. The displacement of these lines is useful to find the mediastinal pathology#info#"
                                                              "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-10-11-41.png#bloquear_img#"
                                                              "#con#Alteration in the paratracheal line.#con#"
                                                              "#webvideo#https://youtu.be/bcPOx08so7A#webvideo#")

        menu.Append(-1, "Inline change to spinal.", "#r#Inline change to spinal.#r#"
                                                              "#info#Mediastinal lines: Mediastinal lines or stripes are interfaces between the soft tissue of mediastinal structures and the lung. The displacement of these lines is useful to find the mediastinal pathology#info#"
                                                              "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-10-11-41.png#bloquear_img#"
                                                              "#con#Inline change to spinal.#con#"
                                                              "#webvideo#https://youtu.be/bcPOx08so7A#webvideo#")

        menu.Append(-1, "Alteration in azo-esophageal recess.", "#r#Alteration in azo-esophageal recess.#r#"
                                                              "#info#Azigoesophageal recess: The most important mediastinal line to be looked for is the azigosophageal line, which delimits the azigoesophageal recess. This line is visible on most front CXRs. The causes of this line's movement are summarized in the table.#info#"
                                                              "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-10-24-37.png#bloquear_img#"
                                                              "#con#Alteration in azo-esophageal recess.#con#"
                                                              "#webvideo#https://youtu.be/ZnkNWUAnXsE#webvideo#")

        menu.Append(-1, "Alteration in aortopulmonary window.", "#r#Alteration in aortopulmonary window.#r#"
                                                              "#info#Aortopulmonary window: The aortopulmonary window is the interface below the aorta and above the pulmonary trunk and is concave or straight laterally. Here, the AP window is convex laterally due to a mass that fills the retrosternal space in the lateral view. On CT images, a mass is observed in the anterior mediastinum. Final diagnosis: Hodgkin's lymphoma. In another very similar case: PET demonstrated the extent of lymph node metastases in this patient. Final diagnosis: small cell lung carcinoma.#info#"
                                                              "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-11-23-32.png#bloquear_img#"
                                                              "#con#Change in aortopulmonary window.Mass that fills the aortopulmonary window.Mass that fills the retrosternal space in the lateral view.#con#"
                                                              "#webvideo#https://youtu.be/bcPOx08so7A#webvideo#")

        menu.Append(-1, "In-line aortic change.", "#r#In-line aortic change.#r#"
                                                              "#info#Mediastinal lines: Mediastinal lines or stripes are interfaces between the soft tissue of mediastinal structures and the lung. The displacement of these lines is useful to find the mediastinal pathology#info#"
                                                              "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-10-11-41.png#bloquear_img#"
                                                              "#con#Change in line for aortic.#con#"
                                                              "#webvideo#https://youtu.be/bcPOx08so7A#webvideo#")


        self.menu_coracao.Append(-1, "Hiatus hernia",
                                 "#r#Retrocardiac opacity with hydroaero level, corresponding to hiatus hernia.#r#"
                                 "#info#Hiatal hernia Dr. Henry Knipe and R Bronson et al. Hiatal hernias occur when there is herniation of the abdominal contents through the esophageal hiatus from the diaphragm to the chest cavity. Epidemiology The prevalence of hiatus hernia increases with age, with a slight female predilection. Clinical presentation Many patients with hiatus hernia are asymptomatic and it is an incidental finding. However, symptoms may include epigastric or chest pain, postprandial fullness, nausea and vomiting 3. Sometimes hiatus hernias are considered synonymous with gastro-oesophageal reflux disease (GERD), but there is a weak correlation between the two conditions. Pathology The most common content of a hiatal hernia is the stomach. There are two main types of hiatal hernia (although they can coexist): sliding hiatal hernia (> 90%) rolling hiatal hernia (paraesophageal) (<10%) Some divide them into four types: type 1: sliding hiatal hernia ( ~ 95%) type 2: paraesophageal hiatal hernia with gastroesophageal junction in normal position type 3: mixed or compound type, paraesophageal hiatal hernia with displaced gastroesophageal junction type 4: mixed or compound hiatal hernia with additional viscera hernia Subtypes Hernia of sliding hiatus This is the most common type of hiatal hernia (~ 90%). The gastroesophageal junction (GOJ) is usually displaced> 2 cm above the esophageal hiatus. The esophageal hiatus is often abnormally enlarged to 3-4 cm (the upper limit of normal is 1.5 cm). The gastric fundus can also be displaced above the diaphragm and present itself as a retrocardiac mass on a chest X-ray. The presence of an air fluid level in the mass suggests the diagnosis. Small sliding hiatus hernias usually decrease in an upright position. The mere presence of a sliding hiatus hernia is of limited clinical significance in most cases. The function of the lower esophageal sphincter and the presence of pathological gastroesophageal reflux are crucial factors to produce symptoms and cause complications. Rolling (para-oesophageal) hiatus hernia Rolling (para-oesophageal) hernia is much less common than the type of sliding. The GOJ remains in its normal location while a part of the stomach hernia above the diaphragm. Mixed rolling and sliding hiatal hernia Mixed or composite hiatal hernia is the most common type of paraesophageal hernia. The GOJ is displaced to the chest with a large portion of the stomach, which is usually abnormally rotated. Radiographic characteristics Radiography simple retrocardiac opacity with hydroaero level Fluoroscopy numerous thick gastric folds within the suprahiatal sac tortuous esophagus with a gastroesophageal junction eccentric CT focal fat collection in the middle mediastinum the hernia omentum through the phrenic-esophageal ligament may see an increase in fat around the distal esophagus para-esophageal hernia through an enlarged esophageal hiatus view contents, size, orientation of the stomach hernia inside the lower thorax herniated content is adjacent to the esophageal enlargement of the esophageal hiatus diaphragmatic cracks (> 15 mm): increase the distance between the crura and the esophageal wall Treatment and prognosis Symptomatic hiatological hernias, especially types 2-4, should be treated surgically 5. Complications Hiatal hernia containing the stomach can result in a gastric volvulus, which in turn presents itself as intestinal obstruction and can result in ischemia / infarction, or very rarely a tension gastrothorax, causing respiratory failure and eventual cardiac arrest. Differential diagnosis On a frontal chest radiography, consider: retrocardiac lung abscess retrocardiac empyema esophageal epiphrenic diverticulum (pulse) phrenic ampoule postoperative change: esophagectomy with gastric pull-up procedure In the scenario of trauma, consider diaphragmatic rupture. https://radiopaedia.org/articles/hiatus-hernia#info#"
                                 "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.04-10-35-27.png#bloquear_img#"
                                 "#con#Retrocardiac opacity with hydroaero level, corresponding to hiatus hernia.#con#"
                                 "#webvideo#https://youtu.be/FoRZNR_qBb0#webvideo#")

        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        return self.plt_btn_anat


    def osso_generico(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="bone", gen="o"):
        """Return customized button. must define
        the position by x and y."""

        nome_anat_ex_direito = nome_anat.split()[-1].replace("direita", "direito").replace("esquerda", "esquerdo")
        nome_anat_ex_direita = nome_anat.split()[-1].replace("direito", "direita").replace("esquerdo", "esquerda")

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0] + nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])

        if "ulna" in nome_anat:
            self.menu_coracao.Append(-1, "Ulnar variance", "#r##variancia_ulnar# ulnar variance.#r#")
            self.menu_coracao.AppendSeparator()


        if "fabela" in nome_anat:
            self.menu_coracao.Append(-1, "Notify presence", "#r#Accessory bone fabela present.#r#"
                                                               "#info#The fabella is an accessory ossicle most always found in the lateral head of the gastrocnemius, rarely can occur at the medial head of gastrocnemius 4. It occurs in ~20% (range 10-30%) of the population website:https://radiopaedia.org/articles/fabella#info#"
                                                               "#con#Accessory bone fabela present.#con#"
                                                               "#bloquear_img#screenshot-img.comunidades.net-2018.07.27-09-30-05.png#bloquear_img#"
                                                               "#webvideo#https://youtu.be/j7JAVEDBxRA#webvideo#")
            self.menu_coracao.AppendSeparator()

        if "Os trigonum" in nome_anat or "Os vesalianum" in nome_anat or "Os peroneum" in nome_anat\
                or "Os intermetatarseum" in nome_anat or "Os tibiale externum" in nome_anat or "Os supranaviculare" in nome_anat\
                or "Os supratalare" in nome_anat:
            self.menu_coracao.Append(-1, "Notify presence", "#r#Accessory bone " + nome_anat + ".#r#"
                                                               "#webvideo#https://youtu.be/yodGed27Y-8#webvideo#")
            self.menu_coracao.AppendSeparator()


        if "medial femoral condyle" in nome_anat or " medial epicondyle" in nome_anat:
            menu = wx.Menu("Eponymous injuries and fractures\tMenu")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Pellegrini-Stieda injuries", "#r#Calcification adjacent to the medial femoral condyle, found according to ossification in the medial collateral ligament ('Pellegrini Stieda lesion') #descrever_correlacionar#.#r#"
                                                           "#info#Pellegrini-Stieda lesion Dr. Ian Bickle and Dr. Behrang Amini et al. Pellegrini-Stieda lesions are post-traumatic lesions ossified at (or near) the medial femoral collateral ligament adjacent to the margin of the medial femoral condyle. A presumed mechanism of injury is a Stieda fracture (avulsion injury of the medial collateral ligament in the medial femoral condyle). Calcification usually begins to form a few weeks after the initial injury. Clinical presentation Most patients are asymptomatic, while a small proportion will have medial knee pain (Pellegrini-Stieda syndrome). Radiographic features Simple radiography Calcification adjacent to the medial femoral condyle, often linear. Magnetic resonance imaging Appears as an ossicle or entheophyte showing bone marrow sign in the medial femoral condyle. The medial collateral ligament is usually thickened. Treatment and prognosis Mild and moderate cases are usually managed conservatively with steroid injections and range of motion exercises. Surgical excision of calcifications and repair of the medial collateral ligament is considered primarily for refractory cases 3 . Differential diagnosis of tendon calcification in reactive arthritis: often presents other degenerative changes History and etymology It was named after the Italian surgeon Augusto Pellegrini (1877-1958) and the German surgeon Alfred Stieda (1869-1945).https://radiopaedia.org/articles/pellegrini-stieda-lesion-1#info#"
                                                           "#bloquear_img#screenshot-radiopaedia.org-2018.08.20-10-46-36.png#bloquear_img#"
                                                           "#con#Characteristic finding of Pellegrini-Stieda lesion.#con#"
                                                           "#webvideo#https://youtu.be/vHn3zY__eR4#webvideo#")
            self.menu_coracao.AppendSeparator()


        if "1st metatarsal" in nome_anat or "distal phalanx of the 1st finger" in nome_anat or "proximal phalanx of the 1st finger" in nome_anat:
            menu = wx.Menu("Measures\tMenu")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Hallux angle", "#r##num_halux_ex_valgo##r#"
                                               "#info#It is the most common foot deformity and is associated with the use of shoes mainly by women.\nSide deviation of the proximal phalanx over the head of the first metatarsal.\nThe angle of the hallux is formed by the line that passes through the axis of the first metatarsal and the line that passes through the axis of the proximal phalanx.\nNormal: 15ºº light hallux valgus: 15-20º moderate hallux valgus: 20-30º severe hallux valgus: 30-45º.#info#"
                                               "#webvideo#https://youtu.be/9idIn28D-U0#webvideo#")
            self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Healthy bone structures.")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Healthy bone structures.", "#r#Healthy bone structures.#r#"
                                                       "#webvideo#https://youtu.be/YoPQr6izL-M#webvideo#")

        menu.Append(-1, "Conserved bone texture.", "#r#Conserved bone texture.#r#"
                                                     "#webvideo#https://youtu.be/LCkhpWTB0ps#webvideo#")

        menu.Append(-1, "Harmonious bone trabeculate.", "#r#Harmonious bone trabeculate.#r#"
                                                         "#webvideo#https://youtu.be/LCkhpWTB0ps#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Other structures without signs of fracture.", "#r#Other structures without signs of fracture.#r#"
                                                                    "#webvideo#https://youtu.be/2HwICXyXav8#webvideo#")
        menu.AppendSeparator()

        menu = wx.Menu("Cortical bone")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Preserved", "#r#" + nome_anat + "  with bone cortical preserved throughout.#r#"
                                                                                                                                       "#webvideo#https://youtu.be/LCkhpWTB0ps#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Fine-tuned throughout", "#r#" + nome_anat + " with cortical fine-tuned throughout #descrever_correlacionar#.#r#"
                                                                                                                                               "#webvideo#https://youtu.be/LCkhpWTB0ps#webvideo#")
        menu.AppendSeparator()
        submenu1 = wx.Menu("Suspected irregularity")
        menu.Append(-1, submenu1.GetTitle(), submenu1)
        submenu1.Append(-1, nome_anat, "#r##descrever_irregularidade_supeita_de_fratura# #descrever_irregularidade_cortical_trabeculado# " + nome_anat + "#descrever_no_contexto_de_trauma##descrever_correlacionar#.#r#"
                                                                                                                                                                                        "#webvideo#https://youtu.be/_Z5eiBK7osA#webvideo#")
        self.menu_coracao.AppendSeparator()

        # pit stop 1

        if "femoral head" in nome_anat:
            menu = wx.Menu("Degeneration|Femoral head|Joint space")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Flat|Reduced|Bilateral", "#r#Accentuated reduction of the hip joint spaces associated with subchondral sclerosis in the acetabular teats and femoral heads.\nLoss of the usual convexity of the femoral heads.#r#"
                                                           "#con#Bilateral thigh associated with loss of the usual convexity of the femoral heads.\nDegenerative changes in the sacroiliac joints.#con#"
                                                           "#webvideo#https://youtu.be/TTCaiElERiA#webvideo#")

            self.menu_coracao.AppendSeparator()
            menu = wx.Menu("Basin\tMenu")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            sub_menu_bas = wx.Menu("Basin Scale")
            menu.Append(-1, sub_menu_bas.GetTitle(), sub_menu_bas)
            sub_menu_bas.Append(-1, "Cranial positioning in relation to the contralateral.", "#r#Bascule of the hip, noting the cranial position of the hip " + nome_anat_ex_direito + " in relation to the contralateral.#r#"
                                                                                                                                                                                         "#webvideo#https://youtu.be/UjpfdQxMsqM#webvideo#")
            sub_menu_bas.AppendSeparator()
            sub_menu_bas.Append(-1, "Discrete | slight cranial positioning relative to the contralateral.", "#r#Discrete pelvic bascule, noting slight cranial hip positioning " + nome_anat_ex_direito + " in relation to the contralateral.#r#"
                                                                                                                                                                                                                       "#webvideo#https://youtu.be/UjpfdQxMsqM#webvideo#")
            self.menu_coracao.AppendSeparator()

            menu = wx.Menu("Measures\tMenu")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Wiberg angle", "#r#Wiberg angle of approximately #num_Wib#º à " + nome_anat_ex_direita + ".#r#"
                                                                                                                                "#webvideo#https://youtu.be/TTCaiElERiA#webvideo#")
            menu.Append(-1, "Wiberg Angle | Bilateral", "#r#Wiberg angle of approximately #num_Wib_d#º on the right and #num_Wib_e# on the left.#r#"
                                                            "#webvideo#https://youtu.be/TTCaiElERiA#webvideo#")
            self.menu_coracao.AppendSeparator()

            menu = wx.Menu("Types of hypercoverage")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Tipo misto (Pincer + CAM) of " + nome_anat_ex_direita, "#r#Signs of acetabular hypercoverage associated with prominence of the superior aspect of the femoral colo-head transition to " + nome_anat_ex_direita + ", may provide some degree of mixed type femoroacetabular impact.#r#")
            menu.Append(-1, "Tipo misto (Pincer + CAM) bilateral", "#r#Signs of acetabular hypercoverage associated with prominence of the superior aspect of the bilateral femoral colo-head transition, which may provide some degree of mixed type femoroacetabular impact.#r#")
            self.menu_coracao.AppendSeparator()

        if "patella" in nome_anat:
            menu = wx.Menu("Measures")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Trochlear groove angle", "#r#Trochlear groove angle of #num_angulo_do_sulco_troclear#º#r#"
                                                        "#info#Furrow angle: angle formed by the lateral (L) and medial (M) facets of the femoral trochlea. Normal: in the radiographic incidence in the axial plane of 30° normal value > 150°.#info#"
                                                        "#bloquear_img#screenshot-www.mskrad.med.br-2018.08.09-17-35-27.png#bloquear_img#"
                                                        "#webvideo#https://youtu.be/K9kMBlTDOCI#webvideo#")



        menu = wx.Menu("Bone Rarefaction")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Diffuse", "#r#Diffuse bone rarefaction signs #descrever_causa_secundaria_da_rarefacao_ossea#.#r#"
                                  "#webvideo#https://youtu.be/LCkhpWTB0ps#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, nome_anat,
                    "#r#Bone rarefaction signal in the " + nome_anat + "#descrever_causa_secundaria_da_rarefacao_ossea#.#r#"
                                                                              "#webvideo#https://youtu.be/LCkhpWTB0ps#webvideo#")
        self.menu_coracao.AppendSeparator()
        menu = wx.Menu("Fracture")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)

        sub_menu = wx.Menu("No signs of fracture")
        menu.Append(-1, sub_menu.GetTitle(), sub_menu)
        sub_menu.Append(-1, "we do not delimit fracture in " + nome_anat, "#r#We do not delimit the aspect of fracture in " + nome_anat + ".#r#"
                                                                                                                                                     "#webvideo#https://youtu.be/797g07r8psQ#webvideo#")
        sub_menu.AppendSeparator()
        sub_menu.Append(-1, "general", "#r#We do not delimit fracture aspect, in the spellings available for analysis.#r#"
                                     "#webvideo#https://youtu.be/Ssql14W0zf8#webvideo#")
        sub_menu.Append(-1, "in this study.", "#r#Bone structures without signs of fracture in this study.#r#"
                                                   "#webvideo#https://youtu.be/X-HF2NBq_d8#webvideo#")
        sub_menu.Append(-1, "Other structures", "#r#Other structures without signs of fracture.#r#"
                                                 "#webvideo#https://youtu.be/Ssql14W0zf8#webvideo#")
        menu.AppendSeparator()

        menu.Append(-1, "Fracture of " + nome_anat + " | Specify", "#r#Fracture #descrever_fratura_ex_completa# #tipo_fra_og1# in " + nome_anat + "#tipo_fra_og2#.#r#"
                                               "#bloquear_img#screenshot-www.med-ed.virginia.edu-2018.07.22-17-17-59.png#bloquear_img#"
                                                "#webvideo#https://youtu.be/9aztCffCakE#webvideo#")

        if "radio" in nome_anat or "ulna" in nome_anat:
            sub_menu1 = wx.Menu("Deviation | Angulation | Luxation")
            menu.Append(-1, sub_menu1.GetTitle(), sub_menu1)
            sub_menu1.Append(-1, "Fracture of the " + nome_anat + " with radial deviation.", "#r#Fracture of " + nome_anat + " with radial deviation.#r#"
                                                                                                                                       "#webvideo#https://youtu.be/S97hK4xxQ3Q#webvideo#")
            sub_menu1.Append(-1, "Fracture of the " + nome_anat + " with ulnar deviation.", "#r#Fracture of " + nome_anat + " with ulnar deviation.#r#"
                                                                                                                                      "#webvideo#https://youtu.be/PmsK3CmZqKI#webvideo#")
            sub_menu1.Append(-1, "Fracture of the " + nome_anat + " with volar angulation.", "#r#Fracture of " + nome_anat + " with volar angulation.#r#"
                                                                                                                                         "#webvideo#https://youtu.be/S97hK4xxQ3Q#webvideo#")
            sub_menu1.Append(-1, "Fracture of the " + nome_anat + " with dorsal angulation.", "#r#Fracture of " + nome_anat + " with dorsal angulation.#r#"
                                                                                                                                          "#webvideo#https://youtu.be/PmsK3CmZqKI#webvideo#")
            sub_menu1.Append(-1, "Fracture of the " + nome_anat + " with distal radioulnar dislocation.", "#r#Fracture of " + nome_anat + " with distal radioulnar dislocation.#r#"
                                                                                                                                                   "#webvideo#https://youtu.be/S97hK4xxQ3Q#webvideo#")
            sub_menu1.Append(-1, "Fracture of the " + nome_anat + " with dislocation of the radio head.", "#r#Fracture of " + nome_anat + " with dislocation of the radio head.#r#"
                                                                                                                                                    "#webvideo#https://youtu.be/PmsK3CmZqKI#webvideo#")

        if "calcaneus" in nome_anat:
            self.menu_coracao.AppendSeparator()
            menu_cal = wx.Menu("Entesophites")
            self.menu_coracao.Append(-1, menu_cal.GetTitle(), menu_cal)
            menu_cal.Append(-1, "Entesophysis of Achilles tendon insertion in the calcaneus.", "#r#Entesophyte #descrever_grau_ex_incipientes_singular_masculino# in the insertion of the Achilles tendon into the calcaneus.#r#"
                                                                                             "#webvideo#https://youtu.be/oRQFu7vWkwI#webvideo#")
            menu_cal.Append(-1, "Entesophyte in the origin of the plantar fascia in the calcaneus.", "#r#Entesophyte #descrever_grau_ex_incipientes_singular_masculino# at the origin of the plantar fascia in the calcaneus.#r#"
                                                                                        "#webvideo#https://youtu.be/oRQFu7vWkwI#webvideo#")
            menu_cal.Append(-1, "Entesophyte in the insertion of the Achilles tendon into the calcaneus and the origin of the plantar fascia.", "#r#Entesophyte #descrever_grau_ex_incipientes_singular_masculino# the insertion of the Achilles tendon into the calcaneus and the origin of the plantar fascia.#r#"
                                                                                                      "#webvideo#https://youtu.be/oRQFu7vWkwI#webvideo#")
            self.menu_coracao.AppendSeparator()

        if "olecranon" in nome_anat:
            self.menu_coracao.AppendSeparator()
            menu_cal = wx.Menu("Entesophitesf")
            self.menu_coracao.Append(-1, menu_cal.GetTitle(), menu_cal)
            menu_cal.Append(-1, "Entesophites in the insertion of the triceps tendon.")
            menu_cal.AppendSeparator()
            menu_cal.Append(-1, "Spur at the tip of the olecranon.")
            self.menu_coracao.AppendSeparator()

        menu.AppendSeparator()
        submenu1 = wx.Menu("Suspicious Irregularity")
        menu.Append(-1, submenu1.GetTitle(), submenu1)
        submenu1.Append(-1,  nome_anat, "#r##descrever_irregularidade_supeita_de_fratura# #descrever_irregularidade_cortical_trabeculado# " + nome_anat + "#descrever_no_contexto_de_trauma##descrever_correlacionar#.#r#"
                                                                                                                                                                                        "#webvideo#https://youtu.be/X-HF2NBq_d8#webvideo#")
        menu.AppendSeparator()

        submenu1 = wx.Menu("Bone fragment")
        menu.Append(-1, submenu1.GetTitle(), submenu1)
        submenu1.Append(-1, "Designed in adjacent soft parts", "#r#Bone fragment projected in soft parts adjacent to " + nome_anat + ".#r#"
                                                                                                                                               "#webvideo#https://youtu.be/797g07r8psQ#webvideo#")
        submenu1.AppendSeparator()
        submenu1.Append(-1, "Diminute | projected in adjacent soft parts | to the base", "#r#Diminute bone fragment projected in soft tissues adjacent to the base of the " + nome_anat + ".#r#"
                                                                                                                                                                                              "#webvideo#https://youtu.be/797g07r8psQ#webvideo#")

        if "humerus" in nome_anat:
            menu.AppendSeparator()
            sub_menu2 = wx.Menu("Indirect signals")
            menu.Append(-1, sub_menu2.GetTitle(), sub_menu2)
            sub_menu2.Append(-1, "Candle Sign | Elbow",
                             "#r#Elevation of the anterior fat pad in the humerus concavity ('candle sign') probably resulting from joint effusion, may be an indirect sign of supracondylar fracture and, in clinical judgment, computed tomography is indicated for better evaluation#r#"
                             "#webvideo#https://youtu.be/PmsK3CmZqKI#webvideo#")

        self.menu_coracao.AppendSeparator()
        menu = wx.Menu("Previous fracture")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Describe | " + nome_anat, "#r##descrever_aspecto_de_fratura_pregressa_consolidada# " + nome_anat + ", #descrever_material_em_fratura_sim_não# #descrever_tipo_de_osteossíntese# #descrever_material_em_fratura_tipos# #descrever_integridade_material# #descrever_correlacionar#.#r#"
                                                                                                                                          "#webvideo#https://youtu.be/AmHJKhtJObs#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, nome_anat, "#r##descrever_irregularidade_supeita_de_fratura# #descrever_irregularidade_cortical_trabeculado# " + nome_anat + "#descrever_no_contexto_de_trauma##descrever_correlacionar#.#r#"
                                                                                                                                                                                    "#webvideo#https://youtu.be/AmHJKhtJObs#webvideo#")
        self.menu_coracao.AppendSeparator()

        self.menu_coracao.Append(-1, "Subluxation| Luxation", "#r##descrever_luxação_ou_subluxação# #descrever_desvio_direcao# " + nome_anat + ".#r#"
                                                                                                                                                         "#webvideo#https://youtu.be/u4-Zbmuhv4c#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Amputation | Absence")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Absence of the " + nome_anat + ".", "#r#Absence #descrever_selecione_local# " + nome_anat + " and structures connected and arranged distally. #descrever_correlacionar#.#r#")

        menu = wx.Menu("Osteófito")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Marginal Osteophyte", "#r#Marginal Osteophyte #descrever_grau_ex_incipientes_singular_masculino# " + nome_anat +".#r#"
                                                                                                                                                    "#webvideo#https://youtu.be/Aopzt-1dPQQ#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Marginal osteophytes", "#r#Marginal osteophytes #descrever_grau_ex_incipientes_plural_masculino# " + nome_anat +".#r#"
                                                                                                                                                      "#webvideo#https://youtu.be/Aopzt-1dPQQ#webvideo#")
        if "ischial tuberosity" in nome_anat:
            menu.AppendSeparator()
            menu.Append(-1, "Entesophyte in the ischiopubic branch.", "#r#Entesophyte in the ischiopubic branch.#r#"
                                                                "#webvideo#https://youtu.be/UjpfdQxMsqM#webvideo#")
            menu.AppendSeparator()
            menu.Append(-1, "Entesophytes in ischiopubic branches.", "#r#Entesophytes in ischiopubic branches.#r#"
                                                                    "#webvideo#https://youtu.be/UjpfdQxMsqM#webvideo#")

        if "iliac" in nome_anat:
            menu.AppendSeparator()
            menu.Append(-1, "Entesophytes in the iliac wing " + nome_anat_ex_direita + ".", "#r#Entesophites #descrever_grau_ex_incipientes_plural_masculino# on the iliac wing " + nome_anat_ex_direita + ".#r#"
                                                                                                                                                                                                 "#webvideo#https://youtu.be/HFioyVRx6vM#webvideo#")
            menu.AppendSeparator()
            menu.Append(-1, "Entesófitos nas asas ilíacas.", "#r#Entesófitos #descrever_grau_ex_incipientes_plural_masculino# nas asas ilíacas.#r#"
                                                             "#webvideo#https://youtu.be/HFioyVRx6vM#webvideo#")

        if "patella" in nome_anat:
            menu.Append(-1, "Osteophytes on the posterior edges of the patella.", "#r#Osteophytes on the posterior edges of the patella.#r#"
                                                                            "#webvideo#https://youtu.be/Aopzt-1dPQQ#webvideo#")
            menu.AppendSeparator()
            menu.Append(-1, "Osteophytes | tibial plateau, femoral condyles and posterior patella edges", "#r#Osteophytes in the tibial plateau, femoral condyles and posterior edges of the patella.#r#"
                                                                                                             "#con#Gonarthrosis signs, as described.#con#"
                                                                                                             "#webvideo#https://youtu.be/Aopzt-1dPQQ#webvideo#")
            menu.AppendSeparator()
            menu.Append(-1, "Entesophyte in the quadriceps insertion.", "#r#Entesophyte in the quadriceps insertion.#r#"
                                                                     "#webvideo#https://youtu.be/Aopzt-1dPQQ#webvideo#")
            menu.AppendSeparator()
            menu.Append(-1, "Entesophysis in the insertion of the patellar tendon in the tibial tuberosity.")

        if "olecranon" in nome_anat:
            menu.AppendSeparator()
            menu.Append(-1, "Entesophites in the insertion of the triceps tendon.")
            menu.AppendSeparator()
            menu.Append(-1, "Spur at the tip of the olecranon.")

        if "tibia" in nome_anat or "femoral condyle" in nome_anat:
            menu.AppendSeparator()
            menu.Append(-1, "Osteophytes | tibial plateau, femoral condyles and posterior patella edges", "#r#Osteophytes in the tibial plateau, femoral condyles and posterior edges of the patella.#r#"
                                                                                                             "#webvideo#https://youtu.be/Aopzt-1dPQQ#webvideo#")
        self.menu_coracao.AppendSeparator()

        if "acetabular" in nome_anat:
            self.menu_coracao.Append(-1, "Sclerosis",
                                     "#r##descrever_grau_ex_incipientes_singular# subchondral sclerosis " + nome_anat + ".#r#"
                                                                                                                                    "#webvideo#https://youtu.be/HFioyVRx6vM#webvideo#")
        else:
            self.menu_coracao.Append(-1, "Sclerosis", "#r##descrever_grau_ex_incipientes_singular# sclerosis " + gen + " " + nome_anat + ".#r#"
                                                                                                                                          "#webvideo#https://youtu.be/TTCaiElERiA#webvideo#")

        if "acetabular" in nome_anat or "acetabular" in nome_anat:
            menu.AppendSeparator()
            menu.Append(-1, "Labral calcification", "#r##descrever_grau_ex_diminuta_singular_feminino# calcification projected in acetabular labrum topography " + nome_anat_ex_direito + ".#r#"
                                                                                                                                                     "#webvideo#https://youtu.be/TTCaiElERiA#webvideo#")

        self.menu_coracao.AppendSeparator()

        if "glenoid" in nome_anat:
            menu = wx.Menu("Eponym fractures")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Bankart's injuries", "#r#A small bone fragment is displaced from the inferior aspect of glenoid, consistent with a Bankart's lesion.#r#"
                                                 "#info#Bankart's lesion Dr. Yuranga Weerakkody and A.Prof Frank Gaillard et al. Bankart's lesions are a common complication of anterior shoulder dislocation and are often seen in association with a Hill-Sachs lesion. Pathology They result from detachment of the anterior lower lip from the underlying glenoid as a direct result of compression of the previously dislocated humerus head against the lip. It may be just labral ('Soft Bankart'), or involve the margin of the bony glenoid (impaction fracture) and this is called 'Bone Bankart'. Soft Bankart's lesions are more common than Bankart's 5 bone lesions. In addition, the anteroinferior labral lesion may extend upwards or downstream. Associations The same compression mechanism can result in a Hill-Sachs lesion. Bankart and Hill-Sachs lesions are 11 times more likely to occur together than isolated 5 lesions. Perthes lesion variants of the shoulder : rupture of the glenoid lip, but with intact periosteum 2 anterior labroligament avulsion in the periosteal sac (ALPSA): mobilized lip remains attached to the glenoid periosteum Radiographic features Simple radiography Bankart's bone lesion can be seen as an anteroinferior glenoid 4 CT aspect fracture without contrast, a fracture can be seen in the anteroinferior glenoid aspect (i.e., Bankart bone) CT arthrography can demonstrate labial avulsion (i.e., Bankart bone), Bankart soft) 4 Magnetic resonance imaging anterior glenoid lip displaced with high intensity bone T2 / PD linear crossing the antero-inferior labrum of abnormally small or absent signal 3 the double axillary pocket signal in the coronal MRI arthrogram is a specific signal for an anteroinferior lip lesion Treatment and prognosis Bankart's lesions heal and therefore early surgical intervention (if any) is not necessary. In Bankart's repairs, the labral fragment is sutured back to the glenoid edge using suture anchors. Differential diagnosis A number of closely related lesions have similar appearances, see previous glenohumeral lesion for discussion of the differences. History and etymology Is named after Arthur Sydney Blundell Bankart , British orthopedic surgeon.https://radiopaedia.org/articles/bankart-lesion#info#"
                                                 "#bloquear_img#screenshot-radiopaedia.org-2018.08.18-18-21-53.png#bloquear_img#"
                                                 "#con#Characteristic finding of Bankart's glenoid lesion.#con#"
                                                 "#webvideo#https://youtu.be/Uvbv46QlFLU#webvideo#")

        menu = wx.Menu("Bone lesions | benign")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Absence of focal bone lesions.", "#r#Absence of focal bone lesions.#r#"
                                                             "#webvideo#https://youtu.be/qxqgkHJj5QI#webvideo#")
        menu.AppendSeparator()
        # Adicionar local seleção
        menu.Append(-1, "Hypotransparent | Delimited | Unspecific aspect", "#r#Heterogeneity of bone trabeculum " + gen + " " + nome_anat + ", observing a hypotransparent, well delimited area, non-specific to the method. At clinical criteria, continue investigation.#r#"
                                                                                                                                                      "#webvideo#https://youtu.be/oFYYZfDw6nA#webvideo#")
        menu.Append(-1, "Bone islet | Decreased radiopaque image", "#r#Small radiopaque image, projected " + nome_anat + ", This may be the bone islet.#r#")
        menu.AppendSeparator()
        menu.Append(-1, "Fibrous cortical defect in " + nome_anat, "#r#There is an incidental lucidity well circumscribed in the " + nome_anat +" measuring less than 2.0 cm. It has a well defined sclerotic edge, without periosteal reaction and without matrix mineralization. Characteristic appearance of a fibrous cortical defect.#r#"
                                                                                                                                                    "#webvideo#https://youtu.be/Xq6GzHvAgG0#webvideo#")

        menu.Append(-1, "Fibrous dysplasia in " + nome_anat, "#r#Presence of well-defined lytic lesion in the " + nome_anat +", with a halo of reactional sclerosis adjacent to and respecting the cortical. Characteristic appearance of fibrous dysplasia.#r#"
                                                                                                                                      "#info#Fibrous dysplasia is a benign, pseudotumoral osteofibrous lesion characterized by the replacement of normal bone by fibrous tissue permeated by a heterogeneous trabeculate of immature bone tissue. It may be solitary or multiple and affects the immature skeleton(1,2). Frequently asymptomatic, this lesion can be diagnosed in adult age by occasional radiological examination, by gradual bone deformity, or in the form of a pathological fracture during childhood. With age, the lesion tends to gradually deform the affected long bones. Radiologically, they are radiotransparent lesions with an intralesional aspect characteristic of 'frosted glass', with precise limits and a narrow transition zone, sometimes with a halo of reactional sclerosis characterizing the so-called 'ring sign'. The main differential diagnosis is with the simple bone cyst. The findings by conventional radiology are presumptive. The histopathological examination confirms the diagnosis.#info#"
                                                                                                                                      "#con#Fibrous dysplasia in " + nome_anat + ".#con#"
                                                                                                                                      "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-14-30-24.png#bloquear_img#"
                                                                                                                                      "#webvideo#https://youtu.be/qxqgkHJj5QI#webvideo#")
        menu.Append(-1, "Osteoid osteoma in " + nome_anat,
                    "#r#Cortical sclerotic thickening of " + nome_anat + " with an area in lucidity. Characteristic appearance of osteoid osteoma.#r#"
                                                                                       "#webvideo#https://youtu.be/gGn3XhZBSQA#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Simple bone cyst in " + nome_anat, "#r#There is an extensive lytic, central lesion in the " + nome_anat + " which inflates the cortical, with defined contours, short transition zone, with adjacent sclerosis halo and intralesional fibrous beams, compatible with simple bone cyst.#r#"
                                                                                                                                      "#info#The simple bone cyst, of unknown cause, is characterized by a lesion in a single, radiotransparent, well-defined cavity, respecting the adjacent bone cortical, with a halo of sclerosis at the lesion margins(1,2) (Figures 1A and 1B). Typically, they have metaphyseal localization and appear in childhood or adolescence. The fracture is the first clinical manifestation and occurs in up to 70% of cases(1). The clinical diagnosis is presumptive by conventional radiology, but computed tomography (CT) and magnetic resonance imaging (MRI) can better stage the lesion(1,2). The aneurysmal bone cyst has more outstanding radiological characteristics, because it is a lytic, metaphyseal painful lesion that inflates the adjacent, rapidly growing cortical, resulting in little or no halo of perilesional sclerosis. It is an insufflative lesion with hematic content cavities of the bone trabeculate, which results in discrete intralesional osteofibrous traverse, which can be seen in the simple radiograph (Figure 1C). In the anatomopathological study there is a typical presence of blood gaps, limited by septa, osteoclasts with inflammatory infiltrate and multinucleated giant cells, without signs of malignancy.#info#"
                                                                                                                                      "#con#Simple bone cyst in " + nome_anat + ".#con#"
                                                                                                                                      "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-14-40-22.png#bloquear_img#")

        menu.Append(-1, "Aneurysmatic bone cyst in " + nome_anat, "#r#An extremely insuflative, lytic lesion is observed, with a short transition zone, without sclerosis halo, with discrete intralesional beams, and which does not invade the growth plate, located in the " + nome_anat + ". The findings are characteristic of aneurysmal bone cyst.#r#"
                                                                                                                                      "#info#The simple bone cyst, of unknown cause, is characterized by a lesion in a single, radiotransparent, well-defined cavity, respecting the adjacent bone cortical, with a halo of sclerosis at the lesion margins(1,2) (Figures 1A and 1B). Typically, they have metaphyseal localization and appear in childhood or adolescence. The fracture is the first clinical manifestation and occurs in up to 70% of cases(1). The clinical diagnosis is presumptive by conventional radiology, but computed tomography (CT) and magnetic resonance imaging (MRI) can better stage the lesion(1,2). The aneurysmal bone cyst has more outstanding radiological characteristics, because it is a lytic, metaphyseal painful lesion that inflates the adjacent, rapidly growing cortical, resulting in little or no halo of perilesional sclerosis. It is an insufflative lesion with hematic content cavities of the bone trabeculate, which results in discrete intralesional osteofibrous traverse, which can be seen in the simple radiograph (Figure 1C). In the anatomopathological study there is a typical presence of blood gaps, limited by septa, osteoclasts with inflammatory infiltrate and multinucleated giant cells, without signs of malignancy.#info#"
                                                                                                                                      "#con#Aneurysmatic bone cyst in " + nome_anat + ".#con#"
                                                                                                                                      "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-14-40-22.png#bloquear_img#"
                                                                                                                                      "#webvideo#https://youtu.be/mKMTkuzj12k#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Bone infarction in " + nome_anat, "#r#The study demonstrates mixed pattern radiological lesion in the " + nome_anat + ", heterogeneous, with geographical aspect and imprecise limits, but that respects the cortical bone. The findings may correspond to bone infarction.#r#"
                                                          "#info#Bone infarction has several causes, such as alcoholism, collagen diseases, use of glucocorticoids or hematological diseases, for example, and may affect all age groups(1-3). The lesions are characterized by necrosis of the spinal bone and loss of normal bone trabeculae, with consequent localized sclerosis. Asymptomatic until it causes joint involvement, bone infarction is frequently found in the presence of investigation for adjacent joint pain(3). In simple radiography, differentiation with encondroma and chondrosarcoma may be difficult. Bone scintigraphy is useful because it assesses whether or not the lesion is metabolically active(2,3). MRI is useful in the evaluation of the lesion extent and in the detailed study of the adjacent joint, as well as in demonstrating typical findings of osteonecrosis. Biopsy is reserved for cases of diagnostic doubt or to exclude true neoplastic lesion(3). At simple radiography, focal or diffuse bone sclerosis is present in one or more bones. Frequently, periarticular metaphyseal involvement is observed. These are mixed lesions, with permeated lytic areas with areas of sclerosis, restricted to the bone marrow, that do not compromise the cortical or induce periosteal reaction (Figure 3).#info#"
                                                          "#con#Findings can correspond to bone infarction in " + nome_anat + ". Magnetic resonance may be required for confirmation.#con#"
                                                          "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-17-17-42.png#bloquear_img#"
                                                          "#webvideo#https://youtu.be/oFYYZfDw6nA#webvideo#")
        menu.AppendSeparator()

        menu.Append(-1, "Osteochondromas in " + nome_anat,
                    "#r#Pedunculated bone growth in the region of the " + nome_anat + ", The epiphysis is eccentrically projected, characteristics that are suggestive of osteochondroma.#r#"
                                                                                                          "#info#Cartilaginous osteochondroma is classically described as the most common benign skeletal tumor, and may be sessile or pediculated, single or multiple, characteristic of familial multiple osteochondromatosis(1-3,5). The patient usually does not complain of pain, but of a bone mass that grows close to a joint, especially the knee. In the specific case of the knee, it may cause limitation of the range of motion and compressive symptoms of peripheral nerves(5). This is a normal bone-forming lesion, surrounded by cartilage, typically metaphyseal, composed of cortical and medullary, centrifugal to the joint, with no signs of radiological aggressiveness (Figure 5). Its important radiological feature is the continuity of its cortical with the cortical of the host bone(6). The growth of osteochondromas is achieved through the cartilaginous layer, similar to the physical plaque, and after skeletal maturity the growth of the lesion also ceases. When there is an increase in the osteochondroma volume after skeletal maturation, a diagnostic investigation should be performed to rule out the possibility of sarcomatous transformation. Transformation to chondrosarcoma is rare, occurring in up to 5% of cases of multiple osteochondromatosis(5,7).#info#"
                                                                                                          "#con#The characteristic findings of osteochondromas in " + nome_anat + ".#con#"
                                                                                                          "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-18-15-24.png#bloquear_img#"
                                                                                                          "#webvideo#https://youtu.be/94hmcpM24aA#webvideo#")

        menu.Append(-1, "Encondroma", "#r#injury in " + nome_anat + " rounded, with small calcification points within the lesion, precise limits and no halo of sclerosis, in the " + nome_anat + ".#r#"
                                "#info#Encondroma: It is a benign tumor characterized by the formation of mature hyaline cartilaginous tissue(1). It may manifest as a solitary or multiple lesion. Frequently it is asymptomatic, more prevalent in the bones of the hand, feet and proximal femur. In the knee, it may be diagnosed at random by a complementary examination directed to another complaint of the patient, or when associated with complications such as pathological fracture (Figure 6)(1,2).#info#"
                                "#con#Characteristic findings of ( Encondroma? ).#con#"
                                "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-18-25-52.png#bloquear_img#"
                                "#webvideo#https://youtu.be/x7aiaG6xipo#webvideo#")

        menu.Append(-1, "Codman Tumor",
                    "#r#Injury in " + nome_anat + " oval, osteolytic, halo of sclerosis, without breaking the cortical, with calcification points inside." + ".#r#"
                                "#info#Also known as Codman's tumor, it is a benign-aggressive bone tumor producing cartilaginous tissue in the epiphysis of the immature skeleton. It presents clinically by periarticular pain and local volume increase in young people with open growth plate. The distal tibia, proximal femur and proximal humerus are the most frequent sites of presentation(1-3). At radiography (Figure 7), well-defined osteolytic epiphyseal lesions with a narrow transition zone, reactive sclerosis halo, that generally does not rupture the cortical and with calcification points inside the lesion, characterizing the cartilaginous lineage of this benign tumor are observed.#info#"
                                "#con#Characteristic findings of ( Chondroblastoma ? ).#con#"
                                "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-22-34-07.png#bloquear_img#"
                                "#webvideo#https://youtu.be/njKG5h4q5c4#webvideo#")

        menu.AppendSeparator()
        menu.Append(-1, "Lytic injury in " + nome_anat + ".", "#r#Lytic injury in " + nome_anat + ".#r#"
                                                                                                  "#webvideo#https://youtu.be/mKMTkuzj12k#webvideo#")
        menu.Append(-1, "Sclerotic injury " + nome_anat + ".", "#r#Sclerotic injury " + nome_anat + ".#r#"
                                                                                                      "#webvideo#https://youtu.be/mKMTkuzj12k#webvideo#")


        menu = wx.Menu("Bone lesions | Descriptor\tMenu")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Describe bone lesion\tSeletor", "#r##descrever_lesão_ossea_tipo# in " + nome_anat + " #descrever_lesão_ossea_2##r#"
                                                                                                              "#webvideo#https://youtu.be/mKMTkuzj12k#webvideo#")

        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Materials | Findings")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Radiotransparent tunnels", "#r#Heterogeneous bone trabeculation in the " + nome_anat + ", noting sparse radiotransparent tunnels, probably related to sites of previous surgical material#r#")

        lista_protese_joelho = ["patela", "côndilo femoral lateral", "côndilo femoral medial", "côndilo lateral da tíbia", "côndilo medial da tíbia", "fêmur distal", "região metafisária da tíbia", "tíbia"]

        if "patella" in nome_anat or "lateral femoral condyle" in nome_anat or "medial femoral condyle" in nome_anat or "lateral condyle of the tibia" in nome_anat or "medial condyle of the tibia" in nome_anat:
            menu.Append(-1, "Total knee prosthesis | Normal", "#r#Presence of total knee prosthesis, with metallic attenuation material, apparently intact and without signs of loosening or displacement.#r#"
                                                                "#webvideo#https://youtu.be/goVX-vAUecI#webvideo#")
            menu.AppendSeparator()
            menu.Append(-1, "Knee Arthroplasty | Evolutionary Control", "#r#Radiological evolution control study shows knee arthroplasty, fixed by screws on the distal third of the femur and by cement on the proximal third of the tibia, with full prosthesis and no signs of loosening.#r#"
                                                                           "#webvideo#https://youtu.be/goVX-vAUecI#webvideo#")
        menu.AppendSeparator()

        if "humeral head" in nome_anat or "humerus" in nome_anat:
            menu.Append(-1, "Shoulder Arthroplasty", "#r#Shoulder arthroplasty composed of glenohumeral prosthesis with intramedullary stem fixed with bone cement.#r#"
                                                     "#webvideo#https://youtu.be/gqitRa4dm1U#webvideo#")

        if "femoral head" in nome_anat or "femoral neck" in nome_anat or "acetabulum" in nome_anat or "acetabular" in nome_anat or "trocanter" in nome_anat:
            menu.Append(-1, "Total hip arthroplasty", "#r#Total hip arthroplasty " + nome_anat_ex_direito + ", composed of articulated femoroacetabular fixation prosthesis, integrated and without signs of loosening.#r#"
                                                                                                                          "#webvideo#https://youtu.be/GfP78DYbOC8#webvideo#")
        menu.AppendSeparator()


        sub_menu = wx.Menu("Immobilization material")
        menu.Append(-1, sub_menu.GetTitle(), sub_menu)
        sub_menu.Append(-1, "Examination performed under immobilization material.", "#r#Examination performed under immobilization material.#r#"
                                                                             "#webvideo#https://youtu.be/10R0FfaFXx4#webvideo#")
        sub_menu.AppendSeparator()
        sub_menu.Append(-1, "Examination performed with plaster splint.", "#r#Examination performed with plaster splint.#r#"
                                                                 "#webvideo#https://youtu.be/10R0FfaFXx4#webvideo#")
        sub_menu.Append(-1, "Examination performed with plaster splint in " + nome_anat , "#r#Examination performed with plaster splint in " + nome_anat + ".#r#")
        sub_menu.AppendSeparator()
        sub_menu.Append(-1, "Presence of orthopedic immobilization material.", "#r#Presence of orthopedic immobilization material.#r#"
                                                                                "#webvideo#https://youtu.be/10R0FfaFXx4#webvideo#")
        sub_menu.Append(-1, "Presence of orthopaedic immobilization material in " + nome_anat , "#r#Presence of orthopaedic immobilization material in " + nome_anat + ".#r#"
                                                                                                                                                                       "#webvideo#https://youtu.be/10R0FfaFXx4#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Cysticercosis", "#r#The X-rays showed calcified lesions embedded in the muscular and subcutaneous tissues with the appearance of a grain of rice whose long axes seem to accompany the planes of the muscular fibers. This is highly suggestive of cysticercosis that occurs by hematogenic dissemination of Taenia solium larvae.#r#"
                                        "#info#The X-rays showed calcified lesions embedded in the muscular and subcutaneous tissues with the appearance of a grain of rice whose long axes seem to accompany the planes of the muscular fibers. This is highly suggestive of cysticercosis that occurs by hematogenic dissemination of Taenia solium larvae.#info#"
                                        "#bloquear_img#screenshot-www.spmi.pt-2018.06.27-16-07-37.png#bloquear_img#"
                                        "#con#Calcified lesions embedded in muscle tissue, highly suggestive of cysticercosis and hematogenic dissemination of Taenia solium larvae.#con#"
                                        "#webvideo#https://youtu.be/CF5E-v02o7Q#webvideo#")
        self.menu_coracao.AppendSeparator()
        menu = wx.Menu("Moles Parts")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Absence of abnormality", "#r#Absence of abnormalities #descrever_grau_ex_signigicativas_plural# in soft parts.#r#")
        menu.AppendSeparator()
        menu.Append(-1, "Enlarged", "#r#Increase #descrever_grau_ex_incipientes_singular_masculino# of soft parts adjacent to the " + nome_anat + " #desc_partes_moles_hd##r#")
        menu.AppendSeparator()

        submenu3 = wx.Menu("Images | Foreign body")
        menu.Append(-1, submenu3.GetTitle(), submenu3)
        submenu3.Append(-1, "Images | Body", "#r#Image #descrever_opacidade_imagem#, #descrever_formato_imagem#, #descrever_posicao_osso#, measuring #num_medindo# #desc_corpo_estranho_hd##r#"
                                               "#webvideo#https://youtu.be/Nwl4yrV4F34#webvideo#")
        submenu3.AppendSeparator()
        submenu3.Append(-1, "Coarse radiopaque images | adjacent to the " + nome_anat, "#r#Coarse radiopaque images, projected in soft parts adjacent to the " + nome_anat + " #desc_corpo_estranho_hd#.#r#"
                                                                                                                                                                                                                                            "#webvideo#https://youtu.be/Y6-xwY9RSAk#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Vascular calcifications.", "#r#Vascular calcifications #descrever_grau_ex_incipientes_plural#.#r#"
                                                     "#webvideo#https://youtu.be/oFiavcUH_Kw#webvideo#")

        self.menu_coracao.AppendSeparator()
        submenu2 = wx.Menu("Control and Fixings")
        self.menu_coracao.Append(-1, submenu2.GetTitle(), submenu2)
        submenu2.Append(-1, "Control study", "#r##descrever_tipo_de_estudo_radiografico_ex_pos_cirurgico# #descrever_aspecto_de_fratura_pregressa_consolidada# in " + nome_anat + ", #descrever_material_em_fratura_sim_não# #descrever_tipo_de_osteossíntese# #descrever_material_em_fratura_tipos# #descrever_integridade_material# #descrever_correlacionar#.#r#"
                                                                                                                                                                                                 "#webvideo#https://youtu.be/GdMFn4--yw4#webvideo#")
        submenu2.AppendSeparator()
        submenu2.Append(-1, "Phrase for completion", "#r#Radiographic study of evolutionary control that must be correlated with clinical data and previous examinations.#r#")

        if "sacrum" in nome_anat:
            menu = wx.Menu("Weight carrying line")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Central" , "#r#" + menu.GetTitle() + " central to " + nome_anat + ".#r#")
            menu.Append(-1, "Previous" , "#r#" + menu.GetTitle() + " before the " + nome_anat + ".#r#")
            menu.Append(-1, "Posterior" , "#r#" + menu.GetTitle() + " posterior to " + nome_anat + ".#r#")

        if "sternum" in nome_anat:
            self.menu_coracao.AppendSeparator()
            self.menu_coracao.Append(-1, "Sternorraphic metal wires.")
            self.menu_coracao.AppendSeparator()
            menu = wx.Menu("Pectus")
            menu.Append(-1, "Pectus excavatum.",
                        "#r#Move to the left of the mediastinum and blur the right edge of the heart. In addition, the contour of the descending aorta is lost. The lateral view confirms sternum depression compatible with diagnosis of pectus excavatum.#r#"
                        "#info#It is the most common thoracic wall deformity, responsible for approximately 90% of the cases, occurs in up to 1 in 300-1000 births 1.4 and is more frequent in men (M: F = 3: 1). The opposite deformity is known as pectus carinatum (pigeon breast). Pectus excavatum (chest funnel) is a congenital chest wall deformity characterized by concave depression of the sternum. The compression of the heart causes characteristic findings on the frontal thoracic radiograph of an indistinct right heart edge, decreased heart density and displacement of the heart to the left. The anterior ribs have a steep downward slope, so that the ribs appear heart-shaped. The indistinct right heart border may mimic the pathology of the right middle lobe, but a lateral thoracic radiograph confirms the sternal deformity. Surgical repair is performed in severe cases. Pectus excavatum is usually an isolated anomaly, but can be associated with Marfan's syndrome, Noonan's syndrome, fetal alcoholic syndrome and homocystinuria.#info#"
                        "#bloquear_img#screenshot-radiopaedia.org-2018.06.03-13-21-05.png#bloquear_img#"
                        "#con#Frontal and lateral chest radiographs show typical pectus excavatum appearances more easily observed in the lateral projection.#con#")

            menu.Append(-1, "Pectus carinatum.",
                        "#r#Deformity of the thoracic wall in which the sternum is previously projected, compatible with the diagnosis of pectus carinatum, more easily observed in the lateral projection.#r#"
                        "#info#Pectus carinatum , also known as breast pigeon , refers to a deformity of the thoracic wall in which the sternum is previously projected. It is less common than pectus excavatum. There are two patterns of sternal protrusion: chondrogladiolar: protrusion of the middle and lower sternum; chondromanubrial: protrusion of the manubrium and upper sternum (less common); known as Currarino-Silverman syndrome. Clinical presentation: patients may present dyspnea and exercise intolerance. Associations: scoliosis (common), cyanotic congenital heart disease (uncommon), family occurrence is reported at ~ 25%. Radiographic characteristics: A pectus carinatum can be demonstrated in lateral thoracic radiographs or cross-sectional chest image. There are two patterns of sternal protrusion: chondrogladiolar: protrusion of the middle and lower chondromanubrial sternum: protrusion of the manubrium and upper sternum (less common); known as Currarino-Silverman syndrome.#info#"
                        "#bloquear_img#screenshot-radiopaedia.org-2018.06.03-13-57-21.png#bloquear_img#"
                        "#con#Radiography shows typical pectus carinatum appearances, more easily observed in the lateral projection.#con#")
            self.menu_coracao.Append(-1, "Pectus", menu)


        if "iliac crest" in nome_anat:
            menu = wx.Menu("Bi-iliac line")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, menu.GetTitle() + " without inclinations.")
            menu.AppendSeparator()
            menu.Append(-1, menu.GetTitle() + " with bottom slope for " + nome_anat.split()[-1] + ".")


        if "acromion" in nome_anat:
            menu = wx.Menu("Types of acromion")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Bigliani acromion type I.", "#r#Bigliani acromion type I.#r#"
                                                           "#webvideo#https://youtu.be/TcsJOLSYcHg#webvideo#")
            menu.Append(-1, "Bigliani acromion type II.", "#r#Bigliani acromion type II.#r#"
                                                            "#webvideo#https://youtu.be/TcsJOLSYcHg#webvideo#")
            menu.Append(-1, "Bigliani acromion type III.", "#r#Bigliani acromion type III.#r#"
                                                             "#webvideo#https://youtu.be/TcsJOLSYcHg#webvideo#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


    def coluna_toracica(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="thoracic spine"):
        """Return customized button. must define
        the position by x and y."""


        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])

        if "thoracic spine" in nome_anat:
            self.menu_coracao.Append(-1, "Degenerative alterations",
                        "#r#Degenerative alterations #descrever_grau_ex_incipientes_plural# in the thoracic spine #descrever_fratura_em_corpo_vertebral_sim_não# #descrever_fratura_em_corpo_vertebral_quantidade# #descrever_sugestao_de_exame_coluna#.#r#"
                        "#info#In lateral view, spondylosis can mimic a pulmonary mass. Any density in the area of the vertebral bodies should take you to the PA film to look for spondylosis, which is usually located on the right side (arrows). On the left side, the formation of osteophytes is hindered by aortic pulsations.#info#"
                        "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-14-52-53.png#bloquear_img#"
                        "#con#Incipient dorsal spondylosis.#con#"
                        "#webvideo#https://youtu.be/-954rG-EYBs#webvideo#")
            self.menu_coracao.AppendSeparator()

            self.menu_coracao.Append(-1, "Vertebral body height reduction",
                        "#r#Reduction of the height of #descrever_numero_reducao_coluna# dorsal vertebral bodies #single_hd##r#"
                        "#webvideo#https://youtu.be/L_NpAJND_II#webvideo#")
            self.menu_coracao.AppendSeparator()

            menu = wx.Menu("Additional description")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Signs of diffuse bone rarefaction.", "#r#Signs of diffuse bone rarefaction.#r#")
            menu.AppendSeparator()
            menu.Append(-1, "Thoracic spondylosis.", "#r#Thoracic spondylosis.#r#"
                                                     "#webvideo#https://youtu.be/LAHNb5cPCG0#webvideo#")
            menu.AppendSeparator()
            menu.Append(-1, "Syndesmophytes",
                            "#r#Subligamentary ossification in the thoracic spine, giving rise to syndesmophites.#r#"
                            "#info#Subligamentous ossification in thoracic spine, giving rise to syndesmophytes (Find may be related to ankylosing spondylitis).#info#"
                            "#webvideo#https://youtu.be/cfJyFz5lrJY#webvideo#")
            menu.AppendSeparator()
            menu.Append(-1, "Marginal osteophytes in thoracic vertebral bodies.", "#r#Marginal osteophytes in thoracic vertebral bodies.#r#"
                                                                                     "#webvideo#https://youtu.be/B2b-hzK3yD8#webvideo#")
            self.menu_coracao.AppendSeparator()

            menu = wx.Menu("Dorsal Cyphosis")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Physiological", "#r#Dorsal physiological cyphosis.#r#")
            menu.Append(-1, "Discretely increased", "#r#Discrete increase in physiological dorsal kyphosis.#r#")
            menu.Append(-1, "Aumentada", "#r#Increase in physiological dorsal kyphosis.#r#")
            menu.Append(-1, "Rectified", "#r#Rectification of physiological dorsal kyphosis.#r#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


    def espaco_articular(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="articular space", gen="o"):
        """Return customized button. must define
        the position by x and y."""
        nome_anat_ex_direita = nome_anat.split()[-1].replace("right", "right").replace("left", "left")
        nome_anat_ex_direito = nome_anat.split()[-1].replace("right", "right").replace("left", "left")

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])
        menu = wx.Menu("Preserved\tMenu ")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Preserved | local", "#r#Articular space in the " + nome_anat + " maintained.#r#"
                                                                                             "#webvideo#https://youtu.be/xb2IK3W9peg#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Preserved | general", "#r#Preserved joint spaces.#r#")
        menu.Append(-1, "Preserved | Others", "#r#Other joint spaces preserved.#r#")
        self.menu_coracao.AppendSeparator()

        # Espaço do joelho
        desc_comp_joelho = ""
        if "compartment" in nome_anat.split()[0] or "knee" in nome_anat.split()[-1]:
            desc_comp_joelho = "#descrever_locais_joelho#"
            self.menu_coracao.Append(-1, "Reduction",
                                     "#r##descrever_grau_ex_leve# redução do espaço articular na " + desc_comp_joelho + ", #descrever_espaco_art##r#"
                                                                                                                                  "#webvideo#https://youtu.be/Aopzt-1dPQQ#webvideo#")
        else:
            self.menu_coracao.Append(-1, "Reduction", "#r##descrever_grau_ex_leve# reduction of joint space " + nome_anat + ", #descrever_espaco_art##r#"
                                                                                                                                          "#webvideo#https://youtu.be/Aopzt-1dPQQ#webvideo#")
        self.menu_coracao.AppendSeparator()

        self.menu_coracao.Append(-1, "Subluxation| Luxation", "#r##descrever_luxação_ou_subluxação# #descrever_desvio_direcao# "+ gen + " " + nome_anat + ".#r#"
                                                                                                                                                         "#webvideo#https://youtu.be/2zgPIgs_ywE#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Separation of the Articulation")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Separation in "+ nome_anat + ".")
        menu.AppendSeparator()
        menu.Append(-1, "Separation in "+ nome_anat + ", for probable ligament rupture.", "#r#Separation in "+ nome_anat + ", for probable ligament rupture.#r#"
                                                                                                                                               "#webvideo#https://youtu.be/O1vddKyo5gQ#webvideo#")
        self.menu_coracao.AppendSeparator()

        self.menu_coracao.Append(-1, "Degenerative alterations", "#r#Degenerative alterations #descrever_grau_ex_leves_plural# "+ nome_anat + " #descrever_espaco_art_alterações_degenerativas##r#"
                                                                                                                                                            "#webvideo#https://youtu.be/Aopzt-1dPQQ#webvideo#")

        if "limpfemoral joint" in nome_anat:
            self.menu_coracao.AppendSeparator()
            self.menu_coracao.Append(-1, "Deep Thigh | Protruse", "#r##descrever_coxa_profunda_ou_protusa_fundos# #descrever_coxa_profunda_ou_protusa#.#r#"
                                                                     "#webvideo#https://youtu.be/OJKTegJtCxo#webvideo#")

        if "side knee compartment" in nome_anat:
            self.menu_coracao.AppendSeparator()
            menu = wx.Menu("Meniscus calcification")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Radiopaque linear image | meniscus calcification", "#r#Radiopaque linear image, projected in the lateral femorotibial joint space, which may be meniscus calcification.#r#"
                                                                                 "#webvideo#https://youtu.be/KTVcVR1dFvQ#webvideo#")

        if "medial knee compartment" in nome_anat:
            menu = wx.Menu("Meniscus calcification")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Radiopaque linear image | meniscus calcification", "#r#Radiopaque linear image projected in the medial femorotibial joint space, which may be meniscus calcification.#r#"
                                                                                 "#webvideo#https://youtu.be/KTVcVR1dFvQ#webvideo#")

        if "compartment" in nome_anat.split()[-1] or "knee" in nome_anat.split()[1]:
            menu = wx.Menu("Sclerosis")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Subchondral sclerosis on the tibial plateau " + nome_anat.split()[0] + ".", "#r#Subchondral sclerosis on the tibial plateau " + nome_anat.split()[0] + ".#r#"
                                                                                                                                                                      "#webvideo#https://youtu.be/Aopzt-1dPQQ#webvideo#")

        if "intercarpal joint" in nome_anat:
            self.menu_coracao.AppendSeparator()
            menu = wx.Menu("Pathologies ")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Rheumatoid Arthritis", "#r#Strong intercarpal degenerative changes with cortical bone sclerosis, areas of bone demineralization and significant reduction of joint space, causing loss of characteristics of the Gilula arches.#r#"
                                                  "#webvideo#https://youtu.be/hRaD9pRtqZ8#webvideo#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


    def forame(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="articular space", gen="o"):
        """Return customized button. must define
        the position by x and y."""


        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])

        self.menu_coracao.Append(-1, "Space maintained", "#r#Space of the " + nome_anat + " maintained.#r#")
        self.menu_coracao.Append(-1, "Reduced space", "#r#Space of the " + nome_anat + " reduced.#r#")
        self.menu_coracao.Append(-1, "Committed space", "#r#Space of the " + nome_anat + " damaged and reduced.#r#")
        self.menu_coracao.Append(-1, "Space with impaired evaluation", "#r#Space of the " + nome_anat + " with impaired evaluation.#r#")
        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat

    def seio_nasal(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="sinus", gen="o"):
        """Return customized button. must define
        the position by x and y."""

        nome_anat_plural = nome_anat.replace("right", "").replace("left", "").replace("Sinus", "Sinus").replace("sinus", "sinus").replace("front", "front").replace("jaw", "jaws").replace("ethmoidal", "ethmoidals").strip()
        nome_anat_ex_direita = nome_anat.split()[0].replace("right", "right").replace("left", "left")


        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])

        menu = wx.Menu("Normal radiological examination")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Exam without particularities.", "#r#Radiological examination without particularities.#r#")
        menu.Append(-1, "Rest of the radiological examination without particularities.", "#r#Rest of the radiological examination without particularities.#r#")
        menu.AppendSeparator()
        menu.Append(-1, "Consistent transparency of the paranasal sinuses.", "#r#Consistent transparency of the paranasal sinuses.#r#"
                                                                          "#webvideo#https://youtu.be/xZYzoB0gGCM#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Preserved | other", "#r#Transparency preserved from other sinuses.#r#"
                                               "#webvideo#https://youtu.be/xZYzoB0gGCM#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Pneumatization")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Pneumatics | age compatible | General", "#r#Face breasts with age-compatible pneumatization.#r#"
                                                                                 "#bloquear_img#screenshot-alimentosaudeinfantil.files.wordpress.com-2018.08.10-12-14-18.png#bloquear_img#"
                                                                                 "#webvideo#https://youtu.be/ldYKjNL8qG0#webvideo#")
        menu.Append(-1, nome_anat_plural[0].title() + nome_anat_plural[1:] + " non pneumatized, age-compatible", "#r#" + nome_anat_plural[0].title() + nome_anat_plural[1:] + " not pneumatized, compatible with the age range.#r#"
                                                                                                                                          "#bloquear_img#screenshot-alimentosaudeinfantil.files.wordpress.com-2018.08.10-12-14-18.png#bloquear_img#"
                                                                                                                                                                                               "#webvideo#https://youtu.be/ldYKjNL8qG0#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, nome_anat[0].title() + nome_anat[1:] + " with the usual pneumatization for the age group.", "#r#"+ nome_anat[0].title() + nome_anat[1:] + " with the usual pneumatization for the age group.#r#"
                                                                                                                                                                 "#webvideo#https://youtu.be/ldYKjNL8qG0#webvideo#")
        self.menu_coracao.AppendSeparator()

        submenu1 = wx.Menu("Hypotransparency\tMenu")
        self.menu_coracao.Append(-1, submenu1.GetTitle(), submenu1)
        submenu1.Append(-1, "Hypotransparency of " + nome_anat + ".", "#r#Hypotransparency of " + nome_anat + " #desc_opa_sinus_hd#.#r#"
                                                                                                                                    "#webvideo#https://youtu.be/xZYzoB0gGCM#webvideo#")
        submenu1.Append(-1, "Hypotransparency of "  + nome_anat_plural + ".", "#r#Hypotransparency of "  + nome_anat_plural + " #desc_opa_sinus_hd#.#r#"
                                                                                                                                                    "#webvideo#https://youtu.be/xZYzoB0gGCM#webvideo#")
        submenu1.AppendSeparator()
        submenu1.Append(-1, "Hypotransparency of " + nome_anat + " | associado a...", "#r#Hypotransparency of " + nome_anat + " #descrever_associação_sinusite# #descrever_locais_seios_da_face# #desc_opa_sinus_hd#.#r#"
                                                                                                                                                    "#webvideo#https://youtu.be/xZYzoB0gGCM#webvideo#")
        submenu1.Append(-1, "Hypotransparency of "  + nome_anat_plural + " | associado a...", "#r#Hypotransparency of "  + nome_anat_plural + " #descrever_associação_sinusite# #descrever_locais_seios_da_face# #desc_opa_sinus_hd#.#r#"
                                                                                                                                                                    "#webvideo#https://youtu.be/xZYzoB0gGCM#webvideo#")
        self.menu_coracao.AppendSeparator()

        submenu1 = wx.Menu("Mucous thickening\tMenu")
        self.menu_coracao.Append(-1, submenu1.GetTitle(), submenu1)
        submenu1.Append(-1, "Mucous thickening of the " + nome_anat + ".", "#r#Mucous thickening of the " + nome_anat + " #desc_opa_sinus_espesamento_mucoso_hd#.#r#"
                                                                                                                                        "#webvideo#https://youtu.be/xZYzoB0gGCM#webvideo#")
        submenu1.Append(-1, "Mucous thickening of the " + nome_anat_plural + ".", "#r#Mucous thickening of the " + nome_anat_plural + " #desc_opa_sinus_espesamento_mucoso_hd#.#r#"
                                                                                                                                                        "#webvideo#https://youtu.be/xZYzoB0gGCM#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Hypoplasia | Agenesis")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Hypoplasia of " + nome_anat + ".", "#r#Hypoplasia of " + nome_anat + ".#r#"
                                                                                                                  "#webvideo#https://youtu.be/ldYKjNL8qG0#webvideo#")
        if "frontal" in nome_anat or "jaw" in nome_anat or "ethmoidal" in nome_anat:
            menu.Append(-1, "Hypoplasia of " + nome_anat_plural + ".", "#r#Hypoplasia of " + nome_anat_plural + ".#r#"
                                                                                                                                                  "#webvideo#https://youtu.be/ldYKjNL8qG0#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Agenesis of " + nome_anat + ".", "#r#Agenesis of " + nome_anat + ".#r#"
                                                                                                              "#webvideo#https://youtu.be/ldYKjNL8qG0#webvideo#")
        if "front" in nome_anat or "jaw" in nome_anat or "ethmoidal" in nome_anat:
            menu.Append(-1, "Agenesis of "  + nome_anat_plural + ".", "#r#Agenesis of " + nome_anat_plural + ".#r#"
                                                                                                                                              "#webvideo#https://youtu.be/ldYKjNL8qG0#webvideo#")
        menu = wx.Menu("Haller Cell")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Haller Cell", "#r#Notes and presence Haller cells#r#"
                                            "#webvideo#https://youtu.be/xcfn9wD4rTQ#webvideo#")

        self.menu_coracao.AppendSeparator()
        menu = wx.Menu("polyp/retention cyst")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Imagem sugestiva de pólipo/cisto de retenção no interior of the " + nome_anat + ".", "#r#Image suggestive of polyps/containment cyst inside the " + nome_anat + ".#r#"
                                                                                                                                                                                                              "#webvideo#https://youtu.be/xZYzoB0gGCM#webvideo#")
        menu = wx.Menu("Haller Cell")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Haller Cell", "#r#Note air cell on orbit floor #descrever_ex_direita_halle#, podendo tratar-se de a Célula de Haller.#r#"
                                            "#webvideo#https://youtu.be/xcfn9wD4rTQ#webvideo#")


        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


    def septo(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="sinus", gen="o"):
        """Return customized button. must define
        the position by x and y."""

        nome_anat_plural = nome_anat.replace("right", "").replace("left", "").replace("Sinus", "Sinus").replace("sinus", "sinus").replace("front", "front").replace("jaw", "jaws").replace("ethmoidal", "ethmoidals").strip()

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])

        self.menu_coracao.Append(-1, nome_anat[0].title() + nome_anat[1:] + " centered.", "#r#"+ nome_anat[0].title() + nome_anat[1:] + " centered.#r#"
                                                                                                                        "#webvideo#https://youtu.be/ldYKjNL8qG0#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Diverted")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "to the right", "#r##descrever_grau_ex_leve_singular_masculino# deviation from " + gen + " " + nome_anat + " to the right.#r#"
                                                                                                                            "#webvideo#https://youtu.be/ldYKjNL8qG0#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "to the left", "#r##descrever_grau_ex_leve_singular_masculino# deviation from " + nome_anat + " to  left.#r#"
                                                                                                                             "#webvideo#https://youtu.be/ldYKjNL8qG0#webvideo#")
        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


    def cavidade_nasal(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="nasal cavity", gen="a"):
        """Return customized button. must define
        the position by x and y."""

        nome_anat_plural = nome_anat.replace("right", "").replace("left", "").replace("right", "").replace("left", "").replace("cavity", "cavities").replace("nasal", "nasal").replace("front", "front").replace("jaw", "jaws").replace("ethmoidal", "ethmoidals").strip()

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])

        menu = wx.Menu("Technical")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Limited evaluation study due to technique and positioning.", "#r#Limited evaluation study due to the technique and positioning.#r#"
                                                                                           "#webvideo#https://youtu.be/_IYfCpBc87Y#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Space maintained")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, nome_anat[0].title() + nome_anat[1:] + " maintained.")

        self.menu_coracao.AppendSeparator()

        if "cavum" in nome_anat:
            self.menu_coracao.Append(-1, "Increase of soft parts", "#r#Increase of soft parts in the rear wall #descrever_locais_rinofaringe#, causing #descrever_grau_de_redução# reduction of the air spine.#r#"
                                                                                                                                                        "#info#Nasopharyngeal radiography (or cavum radiography) is still the most used imaging examination for adenoid size evaluation. Given the variety and complexity of the recommended measurement methods, many radiologists prefer subjective evaluation, which can be inaccurate and not accurate. This review lists and describes the various methods of adenoid radiographic measurement proposed in the literature, considering practicality, accuracy and precision, with the objective of indicating the most adequate ones for daily practice.\nARAUJO NETO, Severino Aires de; QUEIROZ, Suélio Marinho de; BARACAT, Emílio Carlos Elias and PEREIRA, Inês Minniti Rodrigues. Radiographic evaluation of adenoid in children: measurement methods and parameters of normality. Radiol Bras [online]. 2004, vol.37, n.6 [cited 2018-08-15], pp.445-448. Available from: <http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0100-39842004000600012&lng=en&nrm=iso>. ISSN 0100-3984. http://dx.doi.org/10.1590/S0100-39842004000600012.#info#"
                                                                                                                                                        "#bloquear_img#screenshot-www.scielo.br-2018.08.15-13-31-50.png#bloquear_img#"
                                                                                                                                                        "#con#Apparent increase of soft tissues in the posterior wall of the rhinopharynx, causing reduction of the airway spine.#con#"
                                                                    "#webvideo#https://youtu.be/ceAt3gr_JAs#webvideo#")

        if "nasal concha" in nome_anat:
            self.menu_coracao.Append(-1, "Hypertrophy", "#r#Hypertrophy of "+ nome_anat + ", causing #descrever_grau_de_redução# reduction of airspace in the nasal cavity on this side.#r#"
                                                                                                                                                        "#info#Nasopharyngeal radiography (or cavum radiography) is still the most used imaging examination for adenoid size evaluation. Given the variety and complexity of the recommended measurement methods, many radiologists prefer subjective evaluation, which can be inaccurate and not accurate. This review lists and describes the various methods of adenoid radiographic measurement proposed in the literature, considering practicality, accuracy and precision, with the objective of indicating the most adequate ones for daily practice.\nARAUJO NETO, Severino Aires de; QUEIROZ, Suélio Marinho de; BARACAT, Emílio Carlos Elias and PEREIRA, Inês Minniti Rodrigues. Radiographic evaluation of adenoid in children: measurement methods and parameters of normality. Radiol Bras [online]. 2004, vol.37, n.6 [cited 2018-08-15], pp.445-448. Available from: <http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0100-39842004000600012&lng=en&nrm=iso>. ISSN 0100-3984. http://dx.doi.org/10.1590/S0100-39842004000600012.#info#"
                                                                                                                                                        "#bloquear_img#screenshot-www.scielo.br-2018.08.15-13-31-50.png#bloquear_img#"
                                                                                                                                                        "#con#Apparent increase of soft parts in the posterior wall, causing moderate reduction of the air spine.#con#"
                                                                                                                                                                                                                                                "#webvideo#https://youtu.be/ceAt3gr_JAs#webvideo#")



        else:
            self.menu_coracao.Append(-1, "Increase of soft parts", "#r#Increase of the number of parts in the " + nome_anat + "promoting #descrever_grau_de_redução# reduction of the airspace of the nasal cavity on this side.#r#"
                                                                                                                                                        "#info#Nasopharyngeal radiography (or cavum radiography) is still the most used imaging examination for adenoid size evaluation. Given the variety and complexity of the recommended measurement methods, many radiologists prefer subjective evaluation, which can be inaccurate and not accurate. This review lists and describes the various methods of adenoid radiographic measurement proposed in the literature, considering practicality, accuracy and precision, with the objective of indicating the most adequate ones for daily practice.\nARAUJO NETO, Severino Aires de; QUEIROZ, Suélio Marinho de; BARACAT, Emílio Carlos Elias and PEREIRA, Inês Minniti Rodrigues. Radiographic evaluation of adenoid in children: measurement methods and parameters of normality. Radiol Bras [online]. 2004, vol.37, n.6 [cited 2018-08-15], pp.445-448. Available from: <http://www.scielo.br/scielo.php?script=sci_arttext&pid=S0100-39842004000600012&lng=en&nrm=iso>. ISSN 0100-3984. http://dx.doi.org/10.1590/S0100-39842004000600012.#info#"
                                                                                                                                                        "#bloquear_img#screenshot-www.scielo.br-2018.08.15-13-31-50.png#bloquear_img#"
                                                                                                                                                        "#con#Apparent increase of soft parts in the posterior wall causing moderate reduction of the air spine.#con#"
                                                                                                                                                                                                                                                "#webvideo#https://youtu.be/ceAt3gr_JAs#webvideo#")



        if "epiglottis" in nome_anat:
            self.menu_coracao.AppendSeparator()
            self.menu_coracao.Append(-1, "Thickening","#r#Thickening " + nome_anat + " and epiglottic folds are observed with distention of the pharynx and subglottic tracheal narrowing. The findings are in line with epiglottitis.#r#"
                                                                                                      "#info#A epiglotite é uma condição com risco de vida causada pela inflamação da epiglote e pregas ariepiglóticas, que pode levar à obstrução aguda das vias aéreas. Assim, o tratamento deve ser urgente e realizado por indivíduos adequadamente treinados, por exemplo, a instrumentação da traqueia deve ser realizada por um anestesista experiente ou experiente.#info#"
                                                                                                      "#con#As descobertas estão de acordo com a epiglotite.#con#"
                                                                                                      "#bloquear_img#epiglotite_img_radiopedia.png#bloquear_img#"
                                                                                                      "#webvideo#https://youtu.be/chDlfgX75dY#webvideo#")

            self.menu_coracao.Append(-1, "Marked thickening","#r#Marked thickening " + nome_anat + " and epiglottic folds are observed with pharyngeal distension and subglottic tracheal narrowing. The findings are in line with epiglottitis.#r#"
                                                                                                                          "#info#Epiglottis is a life-threatening condition caused by inflammation of the epiglottis and aryepiglottic folds, which can lead to acute airway obstruction. Therefore, treatment should be urgent and performed by suitably trained individuals, for example, instrumentation of the trachea should be performed by an experienced or experienced anesthesiologist.#info#"
                                                                                                                          "#con#The findings are in accordance with the epiglottis.#con#"
                                                                                                                          "#bloquear_img#epiglotite_img_radiopedia.png#bloquear_img#"
                                                                                                                          "#webvideo#https://youtu.be/chDlfgX75dY#webvideo#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat



    def parte_mole(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="soft part", gen="a"):
        """Retorna botão customizado. deve definir
        a posição por x e y."""

        #nome_anat_plural = nome_anat.replace("direito", "").replace("esquerdo", "").replace("Seio", "Seios").replace("seio", "seios").replace("frontal", "frontais").replace("maxilar", "maxilares").replace("etmoidal", "etmoidais").strip()

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])

        if "coxim adiposo" in nome_anat:
            self.menu_coracao.Append(-1, "Obliteration", "#r#obliteration #descrever_grau_ex_incipientes_singular# " + nome_anat + ". It could be joint effusion.#r#"
                                                                                                                                              "#webvideo#https://youtu.be/Aopzt-1dPQQ#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Edema in " + nome_anat + ".")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Emphysema", "#r#Multiple irregular areas of low density within the soft tissues due to emphysema.#r#"
                                                 "#webvideo#https://youtu.be/HQ_RXPo7e_s#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Vascular calcifications.", "#r##descrever_grau_ex_incipientes_plural# vascular calcifications.#r#"
                                                                  "#webvideo#https://youtu.be/oFiavcUH_Kw#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Images | Body", "#r##descrever_opacidade_imagem# image, #descrever_formato_imagem#, #descrever_posicao_mole#, measuring #num_medindo# #desc_corpo_estranho_hd##r#"
                                                        "#webvideo#https://youtu.be/Nwl4yrV4F34#webvideo#")
        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


    def mama(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="mama"):
        """Return customized button. must define
        the position by x and y."""

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0] + nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])
        self.menu_coracao.Append(-1, "nipple " + nome_anat.split()[0].replace("right", "right").replace("left", "left")
                                                  ,"#r#Imagem radiopaca arredondada, podendo tratar-se de ao mamilo " + nome_anat.split()[0].replace("right", "right").replace("left", "left") + ".#r#"
                                                  "#webvideo#https://youtu.be/hC7lI5Z6Wv8#webvideo#")

        self.menu_coracao.Append(-1, "nipples", "#r#Radiopaque images are rounded and may be of the nipples.#r#"
                                                "#webvideo#https://youtu.be/hC7lI5Z6Wv8#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Bilateral breast implant", "#r#Bilateral breast implant is delimited.#r#"
                                                                  "#webvideo#https://youtu.be/dRUss_Gs1CA#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Interposition of more radiopaque breast tissue", "#r#Localized asymmetry of lung transparency, possibly caused by the interposition of more radiopaque breast tissue to the " + nome_anat.split()[0] +".#r#"
                                                                                      "#con#Localized asymmetry of lung transparency, possibly caused by the interposition of the most radiopaque breast tissue.#con#"
                                                                                      "#info#Breast asymmetry Here the breasts are asymmetrical. The underlying lung marks (white boxes) appear denser on the left than on the right. This should not be confused with underlying lung disease. Asymmetry of the breast is very common, even as no breast tissue is visible on one side. It should not be assumed that the patient has had a mastectomy, unless this is known from history.#info#"
                                                                                      "#bloquear_img#screenshot-www.radiologymasterclass.co.uk-2018.07.21-13-04-44.png#bloquear_img#"
                                                                                      "#webvideo#https://youtu.be/AFZtL9OCiIs#webvideo#")
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Lack of shadow on the " + nome_anat + "  (mastectomy?).")

        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Gynecomastia ","#r#Prominent breast shadows bilaterally. (gynecomastia?).#r#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat

    # Coluna Lombar
    def vertebra(self, x=1, y=1, largura=1, altura=1, nome_anat ="C1", gen="o"):
        """Retorna botão customizado. deve definir
        a posição por x e y."""
        nome_anat_ex_lombar = nome_anat.split()[0][0].replace("L", "lumbar").replace("T", "thoracic").replace("S", "sacral").replace("C", "cervical")
        nome_anat_ex_lombares = nome_anat.split()[0][0].replace("L", "lumbar").replace("T", "thoracics").replace("S", "sacrals").replace("C", "cervicals")
        nome_anat = nome_anat.replace("C8", "T1").replace("L0", "T12").replace("L6", "S1")

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])

        menu = wx.Menu("Technical")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        submenu1_1 = wx.Menu("Positioning")
        menu.Append(-1, submenu1_1.GetTitle(), submenu1_1)
        submenu1_1.Append(-1, "lateral", "#r#Radiography with lateral view.#r#"
                                        "#webvideo#https://youtu.be/C-xlBKCdD_o#webvideo#")
        submenu1_1.Append(-1, "AP", "#r#Radiography with AP incidence.#r#"
                                    "#webvideo#https://youtu.be/HMic8YLQrcg#webvideo#")
        submenu1_1.Append(-1, "Oblique incidence", "#r#X-ray with oblique view.#r#"
                                                    "#webvideo#https://youtu.be/dN75c7O1-P0#webvideo#")
        submenu1_1.AppendSeparator()
        submenu1_1.Append(-1, "Transoral", "#r#Radiography with transoral view.#r#"
                                           "#webvideo#https://youtu.be/dN75c7O1-P0#webvideo#")
        submenu1_1.Append(-1, "lateral flexion", "#r#Radiography with lateral view with flexion.#r#"
                                                   "#webvideo#https://youtu.be/dN75c7O1-P0#webvideo#")
        submenu1_1.AppendSeparator()
        submenu1_1.Append(-1, "Hyperflexion", "#r#Radiography with an incidence of hyperflexion.#r#"
                                             "#webvideo#https://youtu.be/dN75c7O1-P0#webvideo#")
        submenu1_1.Append(-1, "Hyperextension", "#r#Radiography with an incidence in hyperextension.#r#"
                                               "#webvideo#https://youtu.be/dN75c7O1-P0#webvideo#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Healthy bone structures.")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Healthy bone structures.", "#r#Healthy bone structures.#r#"
                                                       "#webvideo#https://youtu.be/Q6SWIFd2PNQ#webvideo#")
        menu.Append(-1, "Vertebral bodies with preserved height.", "#r#Vertebral bodies with preserved height.#r#"
                                                                    "#webvideo#https://youtu.be/Q6SWIFd2PNQ#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Conserved bone texture.", "#r#Conserved bone texture.#r#"
                                                     "#webvideo#https://youtu.be/Q6SWIFd2PNQ#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Other structures without signs of fracture.", "#r#Other structures without signs of fracture.#r#"
                                                                    "#webvideo#https://youtu.be/Q6SWIFd2PNQ#webvideo#")
        menu.AppendSeparator()
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Vertebral structures | Bones\tMenu")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        sub_menu = wx.Menu("Vertebral bodies")
        menu.Append(-1, sub_menu.GetTitle(), sub_menu)
        sub_menu.Append(-1, "Vertebral bodies with preserved height.", "#r#Vertebral bodies with preserved height.#r#"
                                                                        "#webvideo#https://youtu.be/Q6SWIFd2PNQ#webvideo#")
        sub_menu.AppendSeparator()
        sub_menu.Append(-1, "Reduction in the height of the vertebral body of " + nome_anat, "#r#Reduction in the height of the vertebral body of " + nome_anat + ", in approximately #num_fra_osteoporose#% #single_hd##r#"
                                                                                                                                                "#webvideo#https://youtu.be/lmwgfracLho#webvideo#")
        if nome_anat == "S1":
            sub_menu.AppendSeparator()
            sub_menu.Append(-1, "Transitional vertebra | lumbarization of S1", "#r#S1 lumbarization (transition vertebra) was considered #complemento_vt##r#")
        if nome_anat == "L5":
            sub_menu.AppendSeparator()
            sub_menu.Append(-1, "Transitional vertebra | sacralization of L5", "#r#The possibility of sacralization of L5 (transition vertebra) was considered #complemento_vt# Megapófises transversas bilaterais em L5 com sinais de neoarticulação sacral, associadas à redução do espaço discal L5-S1, aspectos estes relacionados à assimilação sacral do corpo vertebral de L5.#r#")
            sub_menu.AppendSeparator()
            sub_menu.Append(-1, "Transitional vertebra | sacralization of L5 + hypoplasia of the 12° costal arches", "#r#The possibility of hypoplasia of the 12° costal arches and sacralization of L5 (transition vertebra) were considered #complemento_vt#. Bilateral transverse megaphophysis in L5 with signs of sacral neoarticulation, associated with the reduction of the L5-S1 disc space, aspects related to the sacral assimilation of the vertebral body of L5.#r#")
        sub_menu.AppendSeparator()
        sub_menu1_1 = wx.Menu("partial fusion with hypoplastic disk of vertebral bodies")
        sub_menu.Append(-1, sub_menu1_1.GetTitle(), sub_menu1_1)
        sub_menu1_1.Append(-1, str(nome_anat[0] + str(int(nome_anat[1]) -1) ).replace("L0", "T12") + "-" + nome_anat, "#r#Fusão parcial com disco hipoplásico dos corpos vertebrais de " + str(nome_anat[0] + str(int(nome_anat[1]) -1) ).replace("L0", "T12")+ "-" + nome_anat + ".#r#")
        sub_menu1_1.Append(-1, nome_anat + "-" + str(nome_anat[0] + str(int(nome_anat[1]) + 1) ).replace("L0", "T12"), "#r#Fusão parcial com disco hipoplásico dos corpos vertebrais de " + nome_anat + "-" + str(nome_anat[0] + str(int(nome_anat[1]) + 1) ).replace("L0", "T12") + ".#r#")
        sub_menu.Append(-1, "Schmorl Node", "#r#Small rounded irregularity in the cortical of the vertebral body of " + nome_anat + ". This may correspond to Schmorl's nodule.#r#"
                                                                                                                                          "#webvideo#https://youtu.be/zmEKXy3gCuY#webvideo#")

        menu.AppendSeparator()
        sub_menu = wx.Menu("Posterior Elements")
        menu.Append(-1, sub_menu.GetTitle(), sub_menu)

        if nome_anat[0] == "C":
            sub_menu1_1 = wx.Menu("Pseudofusion of posterior arches")
            sub_menu.Append(-1, sub_menu1_1.GetTitle(), sub_menu1_1)
            sub_menu1_1.Append(-1, "of the cervical spine", "#r#Pseudofusion of posterior cervical spine arches.#r#")

        sub_menu.Append(-1, "Spina bifida hidden in " + nome_anat, "#r#Fusion failure of later elements of " + nome_anat + ", configuring occult spina bifida.#r#"
                                                                                                                                    "#webvideo#https://youtu.be/tdSYdpQL_Mw#webvideo#")
        sub_menu.AppendSeparator()
        sub_menu2 = wx.Menu("Corticalized bone nucleus")
        sub_menu.Append(-1, sub_menu2.GetTitle(), sub_menu2)
        sub_menu2.Append(-1, "in relation to the thorny apophysis of " + nome_anat + " translating accessory core.",
                        "#r#Corticalized bone nucleus is observed in relation to the thorny apophysis of " + nome_anat + ". It may be an accessory core.#r#")

        if "C" in nome_anat[0]:
            sub_menu1 = wx.Menu("Nuchal ligament calcification")
            sub_menu.Append(-1, sub_menu1.GetTitle(), sub_menu1)
            sub_menu1.Append(-1, "Radiopaque, oval-shaped image, projected on soft parts of " + nome_anat,
                             "#r#Radiopaque, oval image, projected in soft parts, after the thorny process of " + nome_anat + ", podendo tratar-se de a calcificação do ligamento nucal.#r#")
            sub_menu1.AppendSeparator()

        menu.AppendSeparator()
        sub_menu = wx.Menu("Interapophysis")
        menu.Append(-1, sub_menu.GetTitle(), sub_menu)
        sub_menu.Append(-1, "Degenerative changes in interapophyseal joints.")

        if "C" not in nome_anat[0]:
            menu.AppendSeparator()
            sub_menu_apt = wx.Menu("Transverse process")
            menu.Append(-1, sub_menu_apt.GetTitle(), sub_menu_apt)
            sub_menu_apt.Append(-1,  nome_anat + " process transverse is enlarged", "#r#" + nome_anat + " process transverse is enlarged #descrever_ex_a_direita_bilateral# #descrever_neoarticulação_sacral#.#r#")
            sub_menu_apt.AppendSeparator()
            sub_menu_apt.Append(-1, "Persistence of the supporting nuclei of " + nome_anat,
                                "#r#Persistence of the supporting cores in the processes across " + nome_anat + ".#r#")

        if "C" in nome_anat[0]:
            menu.AppendSeparator()
            sub_menu_apt = wx.Menu("Cervical ribs")
            menu.Append(-1, sub_menu_apt.GetTitle(), sub_menu_apt)
            sub_menu_apt.Append(-1, "Cervical ribs in " + nome_anat, "#r#Cervical ribs #descrever_ex_a_direita_bilaterais# #descrever_ex_completas# at " + nome_anat + ".#r#")


        menu.AppendSeparator()
        sub_menu_ped = wx.Menu("Pedicles")
        menu.Append(-1, sub_menu_ped.GetTitle(), sub_menu_ped)
        sub_menu_ped.Append(-1, "Unchanged vertebral pedicles.", "#r#Unchanged vertebral pedicles.#r#"
                                                                        "#webvideo#https://youtu.be/nohtLInIqCk#webvideo#")
        sub_menu_ped.AppendSeparator()
        sub_menu_ped.Append(-1, "Absence of the cortical contour of the right pedicle of " + nome_anat + ".", "#r#Absence of the cortical contour of the right pedicle of " + nome_anat + ".#r#"
                                                                                                                                                                                    "#webvideo#https://youtu.be/nohtLInIqCk#webvideo#")
        sub_menu_ped.Append(-1, "Absence of the cortical contour of the left pedicle of " + nome_anat + ".", "#r#Absence of the cortical contour of the left pedicle of " + nome_anat + ".#r#"
                                                                                                                                                                                      "#webvideo#https://youtu.be/nohtLInIqCk#webvideo#")
        sub_menu_ped.AppendSeparator()
        sub_menu_ped.Append(-1, "Absence of the cortical contour of the pedicles of " + nome_anat + ".", "#r#Absence of the cortical contour of the pedicles of " + nome_anat + ".#r#"
                                                                                                                                                                        "#webvideo#https://youtu.be/nohtLInIqCk#webvideo#")
        menu.AppendSeparator()
        sub_menu_for = wx.Menu("Conjugation foramen")
        menu.Append(-1, sub_menu_for.GetTitle(), sub_menu_for)
        sub_menu_for.Append(-1, "Amplitude preserved | General", "#r#The conjugation foramen have intact amplitude.#r#"
                                                                "#webvideo#https://youtu.be/gxmaMcpTs_o#webvideo#")
        sub_menu_for.AppendSeparator()
        sub_menu_for.Append(-1, "Reduction of amplitude | Local", "#r#Reduction of the amplitude of the conjugation foramen in the level #seleção_espaço_vertebral##r#"
                                                                "#webvideo#https://youtu.be/gxmaMcpTs_o#webvideo#")



        if nome_anat[0] == "T":
            menu.AppendSeparator()
            sub_menu_arc = wx.Menu("Coastal arches")
            menu.Append(-1, sub_menu_arc.GetTitle(), sub_menu_arc)
            sub_menu_arc.Append(-1, "Hypoplasia of the " + nome_anat[1:], "#r#Hypoplasia of the " + nome_anat[1:] + "° costal arches #complemento_vt##r#")
            sub_menu_arc.AppendSeparator()
            sub_menu_arc.Append(-1, "Hypoplasia of the " + nome_anat[1:] + " and sacralization of L5 TV", "#r#Hypoplasia of the " + nome_anat[1:] + "° costal arches and sacralization of L5 (transition vertebra) #complemento_vt##r#")
            sub_menu_arc.AppendSeparator()
            sub_menu_arc.Append(-1, "Hypoplasia of " + nome_anat[1:], "#r#Hypoplasia of " + nome_anat[1:] + "° costal arches #complemento_vt##r#")


        if nome_anat[0] == "C":
            menu.AppendSeparator()
            sub_menu = wx.Menu("Unciform processes")
            menu.Append(-1, sub_menu.GetTitle(), sub_menu)
            sub_menu.Append(-1, "Degenerative changes in unciform processes.", "#r#Degenerative alterations #descrever_grau_ex_incipientes_plural# in unciform processes.#r#"
                                                                                      "#webvideo#https://youtu.be/AJPQiu7-VWQ#webvideo#")

        if nome_anat[0] == "C":
            menu = wx.Menu("Moles Parts")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Nuchal ligament sesamoid ossicles", "#r##descrever_tamanho# radiopaque, oval, borderline, corticalized image projected on the topography of the nuchal ligament, posterior to the vertebral bodies of #seleção_espaço_vertebral_sem_ponto_final#, measuring approximately #num_medindo_so_num#mm in its largest axis, which may be the sesamoid ossicles of the nuchal ligament.#r#")


        self.menu_coracao.AppendSeparator()
        menu = wx.Menu("Disk spaces")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        sub_menu = wx.Menu("Preserved")
        menu.Append(-1, sub_menu.GetTitle(), sub_menu)
        sub_menu.Append(-1, "Preserved | general", "#r#Preserved disc spaces.#r#"
                                                   "#webvideo#https://youtu.be/gcvEoTzEXhY#webvideo#")
        sub_menu.Append(-1, nome_anat_ex_lombares.title() + " maintained", "#r#Disk spaces " + nome_anat_ex_lombares + " maintained.#r#"
                                                                                                                         "#webvideo#https://youtu.be/gcvEoTzEXhY#webvideo#")
        sub_menu.Append(-1,"Others " + nome_anat_ex_lombares + " maintained", "#r#Other disc spaces " + nome_anat_ex_lombares + " maintained.#r#"
                                                                                                                                   "#webvideo#https://youtu.be/gcvEoTzEXhY#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Reduction of disc space\tSelector", "#r##descrever_grau_de_redução# reduction of disc space on the level #seleção_espaço_vertebral##r#"
                                                             "#webvideo#https://youtu.be/gcvEoTzEXhY#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Disc space characterization\tSelector", "#r# #descrever_alteracoes_espaco_dis# in the disc space in #seleção_espaço_vertebral##r#"
                                                                    "#webvideo#https://youtu.be/gcvEoTzEXhY#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Diffuse reduction of disc spaces.", "#r#Diffuse reduction of disc spaces.#r#"
                                                               "#webvideo#https://youtu.be/gcvEoTzEXhY#webvideo#")

        menu = wx.Menu("Posterior vertebral alignment")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Preserved", "#r#Posterior vertebral alignment preserved, no signs of listese.#r#"
                                      "#webvideo#https://youtu.be/gxmaMcpTs_o#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Anterolysthesis of " + nome_anat + " above " + str(nome_anat[0] + str(int(nome_anat[1]) +1 )).replace("L0", "T12").replace("L6", "S1").replace("C8", "T1") + ".", "#r#Anterolistese #descrever_grau_listese# of " + nome_anat + " above " + str(nome_anat[0] + str(int(nome_anat[1]) +1 )).replace("L0", "T12").replace("L6", "S1") + ", #descrever_listese_hd##r#"                                                                                                                                                                                                                                                                                                      "#bloquear_img#screenshot-www.mskrad.med.br-2018.08.20-19-20-24.png#bloquear_img#"
                                                                                                                                                                                                                                                                                                                                         "#webvideo#https://youtu.be/gxmaMcpTs_o#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Retrolistese " + nome_anat + " above " + str(nome_anat[0] + str(int(nome_anat[1]) +1 )).replace("L0", "T12").replace("L6", "S1").replace("C8", "T1"), "#r##descrever_listese_acentuacao# retrolistese" + "  of " + nome_anat + " above " + str(nome_anat[0] + str(int(nome_anat[1]) +1 )).replace("L0", "T12").replace("L6", "S1") + ", #descrever_listese_hd##r#"
                                                                                                                                                                                                                                                                                                                                         "#webvideo#https://youtu.be/gxmaMcpTs_o#webvideo#")
        self.menu_coracao.AppendSeparator()


        menu = wx.Menu("Medidas\tMenu")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Ferguson angle", "#r#Ângulo de Ferguson de #num_fer##r#"
                                              "#info#Sacral slope - (sacral slope) reflects the position of the sacrum in space and conditions the degree of lordosis of the lumbar spine. Measured by the angle formed by the upper margin of the body of S1 (red line) and the horizontal plane (black dotted line). Sacral inclination and lumbar lordosis: sacral inclination < 35°NORMAL: inclination 35°-45°NHIPERLORDOSIS: > 45°.#info#"
                                              "#bloquear_img#screenshot-www.mskrad.med.br-2018.08.10-10-14-55.png#bloquear_img#")
        menu.AppendSeparator()
        menu.Append(-1, "Cobb's Angle", "#r#Asymmetry of the longitudinal axis of the spine " + nome_anat_ex_lombar + " with convexity to #descrever_ex_direita_cobb# and Cobb angle of #num_Cobb# graus.#r#"
                                                                                                                       "#info#The scoliosis are classified as light, when they present curvatures between 10º and 20º, moderate between 20º and 40º and severe above 40º.#info#")
        menu.AppendSeparator()
        menu.Append(-1, "Weight carrying line", "#r#Weight carrying line #descrever_linha_porte_de_peso# to the body of S1.#r#")
        menu.AppendSeparator()
        menu.Append(-1, "Weight carrying line | Sacro", "#r#Projection of the weight carrying line #descrever_linha_porte_de_peso_sacro# to the sacrum.#r#")
        menu.AppendSeparator()
        menu.Append(-1, "Absence of significant scholastic deviation.")

        menu = wx.Menu("Curvature")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Physiological", "#r#" + nome_anat_ex_lombar + " #descrever_grau_ex_incipientes_singular# physiological curvature.#r#")
        menu.AppendSeparator()
        menu.Append(-1, "Rectification", "#r#" + nome_anat_ex_lombar + " #descrever_grau_ex_incipientes_singular# physiological curvature rectification.#r#")
        menu.AppendSeparator()
        menu.Append(-1, "Accentuation", "#r#" + nome_anat_ex_lombar + " #descrever_grau_ex_incipientes_singular# accentuation of the physiological curvature.#r#")

        self.menu_coracao.Append(-1, "Longitudinal axis | Inclination", "#r##descrever_grau_ex_leve# inclination of the longitudinal axis of the spine #descrever_ex_para_a_direita##single_hd_inclinacao##r#")
        self.menu_coracao.AppendSeparator()

        menu = wx.Menu("Degenerative alterations")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Degenerative changes in the spine " + nome_anat_ex_lombar + ".", "#r#Degenerative changes in the spine " + nome_anat_ex_lombar + ".#r#"
                                                                                                                        "#webvideo#https://youtu.be/B2b-hzK3yD8#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Signs of diffuse bone rarefaction.", "#r#Signs of diffuse bone rarefaction.#r#"
                                                             "#webvideo#https://youtu.be/B2b-hzK3yD8#webvideo#")
        menu.AppendSeparator()

        submenu1 = wx.Menu("Spondilose")
        menu.Append(-1, submenu1.GetTitle(), submenu1)

        submenu1.Append(-1, "Discrete spondylosis | Reduction and osteophyte", "#r#Discrete spondylosis changes with antero-lateral and posterior osteophytes, reduction of disc space in " + nome_anat + "-" + (nome_anat[0] + str(int(nome_anat[1]) + 1)).replace("L6", "S1").replace("C8", "T1") + " with indirect signs of degenerative discopathy.#r#"
                                                          "#info#In lateral view, spondylosis can mimic a pulmonary mass. Any density in the area of the vertebral bodies should take you to the PA film to look for spondylosis, which is usually located on the right side (arrows). On the left side, the formation of osteophytes is hindered by aortic pulsations.#info#"
                                                          "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-14-52-53.png#bloquear_img#"
                                                          "#con#Incipient dorsal spondylosis.#con#"
                                                          "#webvideo#https://youtu.be/gcvEoTzEXhY#webvideo#")
        submenu1.AppendSeparator()
        submenu1.Append(-1, "Advanced Arthrosis Spondylium", "#r#Exuberant anterior and posterior osteophytes reduction of disc spaces, mainly in " + nome_anat + "-" + (nome_anat[0] + str(int(nome_anat[1]) + 1)).replace("L6", "S1").replace("C8", "T1") + ", bone sclerosis of the posterior elements with interapophyseal arthrosis.#r#"
                                                          "#info#In lateral view, spondylosis can mimic a pulmonary mass. Any density in the area of the vertebral bodies should take you to the PA film to look for spondylosis, which is usually located on the right side (arrows). On the left side, the formation of osteophytes is hindered by aortic pulsations.#info#"
                                                          "#bloquear_img#screenshot-www.radiologyassistant.nl-2018.06.03-14-52-53.png#bloquear_img#"
                                                          "#con#Incipient dorsal spondylosis.#con#"
                                                          "#webvideo#https://youtu.be/gcvEoTzEXhY#webvideo#")

        sub_menu = wx.Menu("Syndesmophytes")
        menu.Append(-1, sub_menu.GetTitle(), sub_menu)
        sub_menu.Append(-1, sub_menu.GetTitle(),
                        "#r#Subligamentary ossification in the thoracic spine, giving rise to syndesmophites.#r#"
                        "#webvideo#https://youtu.be/cfJyFz5lrJY#webvideo#")

        menu = wx.Menu("Bone lesions | benign")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Absence of focal bone lesions.", "#r#Absence of focal bone lesions.#r#"
                                                             "#webvideo#https://youtu.be/qxqgkHJj5QI#webvideo#")
        menu.AppendSeparator()
        # Adicionar local seleção
        menu.Append(-1, "Hypotransparent | Delimited | Unspecific aspect",
                    "#r#Heterogeneity of bone trabeculate in " + nome_anat + ", observing a hypotransparent, well delimited area, non-specific to the method. At clinical criteria, continue investigation.#r#"
                                                                                "#webvideo#https://youtu.be/oFYYZfDw6nA#webvideo#")
        menu.Append(-1, "Bone islet | Decreased radiopaque image",
                    "#r#Small radiopaque image, projected in " + nome_anat + ", This may be the bone islet.#r#")
        menu.AppendSeparator()
        menu.Append(-1, "Fibrous cortical defect in " + nome_anat,
                    "#r#There is an incidental lucidity well circumscribed in " + nome_anat + " measuring less than 2.0 cm. It has a well defined sclerotic edge, without periosteal reaction and without matrix mineralization. Characteristic appearance of a fibrous cortical defect.#r#"
                                                                                           "#webvideo#https://youtu.be/qxqgkHJj5QI#webvideo#")


        menu.Append(-1, "Fibrous dysplasia in " + nome_anat,
                    "#r#Presence of well-defined lytic lesion in " + nome_anat + ", with a halo of reactional sclerosis adjacent to and respecting the cortical. Characteristic appearance of fibrous dysplasia.#r#"
                                                                                              "#info#Fibrous dysplasia is a benign, pseudotumoral osteofibrous lesion characterized by the replacement of normal bone by fibrous tissue permeated by a heterogeneous trabeculate of immature bone tissue. It may be solitary or multiple and affects the immature skeleton(1,2). Frequently asymptomatic, this lesion can be diagnosed in adult age by occasional radiological examination, by gradual bone deformity, or in the form of a pathological fracture during childhood. With age, the lesion tends to gradually deform the affected long bones. Radiologically, they are radiotransparent lesions with an intralesional aspect characteristic of 'frosted glass', with precise limits and a narrow transition zone, sometimes with a halo of reactional sclerosis characterizing the so-called 'ring sign'. The main differential diagnosis is with the simple bone cyst. The findings by conventional radiology are presumptive. The histopathological examination confirms the diagnosis.#info#"
                                                                                              "#con#Displasia fibrosa em " + nome_anat + ".#con#"
                                                                                                                                         "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-14-30-24.png#bloquear_img#"
                                                                                                                                         "#webvideo#https://youtu.be/qxqgkHJj5QI#webvideo#")
        menu.Append(-1, "Osteoid osteoma in " + nome_anat,
                    "#r#Cortical sclerotic thickening in " + nome_anat + " with an area in lucidity. Characteristic appearance of osteoid osteoma.#r#"
                                                                             "#webvideo#https://youtu.be/gGn3XhZBSQA#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Simple bone cyst in " + nome_anat,
                    "#r#An extensive lytic, central lesion is observed in " + nome_anat + " which inflates the cortical, with defined contours, short transition zone, with adjacent sclerosis halo and intralesional fibrous beams, compatible with simple bone cyst.#r#"
                                                                                               "#info#The simple bone cyst, of unknown cause, is characterized by a lesion in a single, radiotransparent, well-defined cavity, respecting the adjacent bone cortical, with a halo of sclerosis at the lesion margins(1,2) (Figures 1A and 1B). Typically, they have metaphyseal localization and appear in childhood or adolescence. The fracture is the first clinical manifestation and occurs in up to 70% of cases(1). The clinical diagnosis is presumptive by conventional radiology, but computed tomography (CT) and magnetic resonance imaging (MRI) can better stage the lesion(1,2). The aneurysmal bone cyst has more outstanding radiological characteristics, because it is a lytic, metaphyseal painful lesion that inflates the adjacent, rapidly growing cortical, resulting in little or no halo of perilesional sclerosis. It is an insufflative lesion with hematic content cavities of the bone trabeculate, which results in discrete intralesional osteofibrous traverse, which can be seen in the simple radiograph (Figure 1C). In the anatomopathological study there is a typical presence of blood gaps, limited by septa, osteoclasts with inflammatory infiltrate and multinucleated giant cells, without signs of malignancy.#info#"
                                                                                               "#con#Simple bone cyst in " + nome_anat + ".#con#"
                                                                                                                                            "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-14-40-22.png#bloquear_img#"
                                                                                                                                            "#webvideo#https://youtu.be/mKMTkuzj12k#webvideo#")

        menu.Append(-1, "Aneurysmatic bone cyst in " + nome_anat,
                    "#r#An extremely insuflative, lytic lesion is observed, with a short transition zone, without sclerosis halo, with discrete intralesional beams, and which does not invade the growth plate, located in the " + nome_anat + ". The findings are characteristic of aneurysmal bone cyst.#r#"
                                                                                                                                                                                                                                                     "#info#The simple bone cyst, of unknown cause, is characterized by a lesion in a single, radiotransparent, well-defined cavity, respecting the adjacent bone cortical, with a halo of sclerosis at the lesion margins(1,2) (Figures 1A and 1B). Typically, they have metaphyseal localization and appear in childhood or adolescence. The fracture is the first clinical manifestation and occurs in up to 70% of cases(1). The clinical diagnosis is presumptive by conventional radiology, but computed tomography (CT) and magnetic resonance imaging (MRI) can better stage the lesion(1,2). The aneurysmal bone cyst has more outstanding radiological characteristics, because it is a lytic, metaphyseal painful lesion that inflates the adjacent, rapidly growing cortical, resulting in little or no halo of perilesional sclerosis. It is an insufflative lesion with hematic content cavities of the bone trabeculate, which results in discrete intralesional osteofibrous traverse, which can be seen in the simple radiograph (Figure 1C). In the anatomopathological study there is a typical presence of blood gaps, limited by septa, osteoclasts with inflammatory infiltrate and multinucleated giant cells, without signs of malignancy.#info#"
                                                                                                                                                                                                                                                     "#con#Aneurysmatic bone cyst in " + nome_anat + ".#con#"
                                                                                                                                                                                                                                                                                                        "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-14-40-22.png#bloquear_img#"
                                                                                                                                                                                                                                                                                                        "#webvideo#https://youtu.be/mKMTkuzj12k#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Bone infarction in " + nome_anat,
                    "#r#The study demonstrates mixed pattern radiological injury in " + nome_anat + "The cortical bone is heterogeneous, with a geographical aspect and imprecise limits, but it respects the cortical bone. The findings may correspond to bone infarction.#r#"
                                                                                                          "#info#Bone infarction has several causes, such as alcoholism, collagen diseases, use of glucocorticoids or hematological diseases, for example, and may affect all age groups(1-3). The lesions are characterized by necrosis of the spinal bone and loss of normal bone trabeculae, with consequent localized sclerosis. Asymptomatic until it causes joint involvement, bone infarction is frequently found in the presence of investigation for adjacent joint pain(3). In simple radiography, differentiation with encondroma and chondrosarcoma may be difficult. Bone scintigraphy is useful because it assesses whether or not the lesion is metabolically active(2,3). MRI is useful in the evaluation of the lesion extent and in the detailed study of the adjacent joint, as well as in demonstrating typical findings of osteonecrosis. Biopsy is reserved for cases of diagnostic doubt or to exclude true neoplastic lesion(3). At simple radiography, focal or diffuse bone sclerosis is present in one or more bones. Frequently, periarticular metaphyseal involvement is observed. These are mixed lesions, with permeated lytic areas with areas of sclerosis, restricted to the bone marrow, that do not compromise the cortical or induce periosteal reaction (Figure 3).#info#"
                                                                                                          "#con#Findings can correspond to bone infarction in " + nome_anat + ". Magnetic resonance may be required for confirmation.#con#"
                                                                                                                                                                                 "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-17-17-42.png#bloquear_img#"
                                                                                                                                                                                 "#webvideo#https://youtu.be/oFYYZfDw6nA#webvideo#")
        menu.AppendSeparator()

        menu.Append(-1, "Osteochondromas in " + nome_anat,
                    "#r#Mixed sessile lesions in the " + nome_anat + "with normal bone appearance, characteristics of osteochondromas.#r#"
                                                                                     "#info#Cartilaginous osteochondroma is classically described as the most common benign skeletal tumor, and may be sessile or pediculated, single or multiple, characteristic of familial multiple osteochondromatosis(1-3,5). The patient usually does not complain of pain, but of a bone mass that grows close to a joint, especially the knee. In the specific case of the knee, it may cause limitation of the range of motion and compressive symptoms of peripheral nerves(5). This is a normal bone-forming lesion, surrounded by cartilage, typically metaphyseal, composed of cortical and medullary, centrifugal to the joint, with no signs of radiological aggressiveness (Figure 5). Its important radiological feature is the continuity of its cortical with the cortical of the host bone(6). The growth of osteochondromas is achieved through the cartilaginous layer, similar to the physical plaque, and after skeletal maturity the growth of the lesion also ceases. When there is an increase in the osteochondroma volume after skeletal maturation, a diagnostic investigation should be performed to rule out the possibility of sarcomatous transformation. Transformation to chondrosarcoma is rare, occurring in up to 5% of cases of multiple osteochondromatosis(5,7).#info#"
                                                                                     "#con#The characteristic findings of osteochondromas in " + nome_anat + ".#con#"
                                                                                                                                                            "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-18-15-24.png#bloquear_img#"
                                                                                                                                                            "#webvideo#https://youtu.be/94hmcpM24aA#webvideo#")

        menu.Append(-1, "Encondroma",
                    "#r#injury in " + nome_anat + " rounded, with small calcification points within the lesion, precise limits and no halo of sclerosis, in the " + nome_anat + ".#r#"
                                                                                                                                                                                            "#info#Encondroma: It is a benign tumor characterized by the formation of mature hyaline cartilaginous tissue(1). It may manifest as a solitary or multiple lesion. Frequently it is asymptomatic, more prevalent in the bones of the hand, feet and proximal femur. In the knee, it may be diagnosed at random by a complementary examination directed to another complaint of the patient, or when associated with complications such as pathological fracture (Figure 6)(1,2).#info#"
                                                                                                                                                                                            "#con#Flattened characteristics of (Encondroma?).#con#"
                                                                                                                                                                                            "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-18-25-52.png#bloquear_img#"
                                                                                                                                                                                            "#webvideo#https://youtu.be/x7aiaG6xipo#webvideo#")

        menu.Append(-1, "Codman Tumor",
                    "#r#Injury in " + nome_anat + " oval, osteolytic, halo of sclerosis, without breaking the cortical, with calcification points inside." + ".#r#"
                                                                                                                                                                  "#info#Also known as Codman's tumor, it is a benign-aggressive bone tumor producing cartilaginous tissue in the epiphysis of the immature skeleton. It presents clinically by periarticular pain and local volume increase in young people with open growth plate. The distal tibia, proximal femur and proximal humerus are the most frequent sites of presentation(1-3). At radiography (Figure 7), well-defined osteolytic epiphyseal lesions with a narrow transition zone, reactive sclerosis halo, that generally does not rupture the cortical and with calcification points inside the lesion, characterizing the cartilaginous lineage of this benign tumor are observed.#info#"
                                                                                                                                                                  "#con#Characteristics of chondroblastoma.#con#"
                                                                                                                                                                  "#bloquear_img#screenshot-www.rb.org.br-2018.07.15-22-34-07.png#bloquear_img#"
                                                                                                                                                                  "#webvideo#https://youtu.be/njKG5h4q5c4#webvideo#")

        menu.AppendSeparator()
        menu.Append(-1, "Lytic injury in " + nome_anat + ".", "#r#Lytic injury in " + nome_anat + ".#r#"
                                                                                                  "#webvideo#https://youtu.be/mKMTkuzj12k#webvideo#")
        menu.Append(-1, "Sclerotic injury " + nome_anat + ".", "#r#Sclerotic injury " + nome_anat + ".#r#"
                                                                                                      "#webvideo#https://youtu.be/mKMTkuzj12k#webvideo#")

        menu = wx.Menu("Bone lesions | Descriptor\tMenu")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Describe bone lesion\tSeletor",
                    "#r##descrever_lesão_ossea_tipo# em " + nome_anat + " #descrever_lesão_ossea_2##r#"
                                                                        "#webvideo#https://youtu.be/mKMTkuzj12k#webvideo#")

        self.menu_coracao.AppendSeparator()
        menu = wx.Menu("Osteófito")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Marginal osteophytes\tSelect", "#r#Marginal osteophytes #descrever_osteofitos# in the vertebral body of #seleção_vertebra##r#"
                                                            "#webvideo#https://youtu.be/B2b-hzK3yD8#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Marginal osteophytes in multiple vertebral bodies.", "#r#Marginal osteophytes #descrever_osteofitos# in multiple vertebral bodies.#r#"
                                                                                "#webvideo#https://youtu.be/B2b-hzK3yD8#webvideo#")

        menu = wx.Menu("Fractures | Lise\tMenu")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)

        submenu_lise = wx.Menu("Isthmic Lysis")
        menu.Append(-1, submenu_lise.GetTitle(), submenu_lise)
        submenu_lise.Append(-1, "Radiolucent trace | sequel of Isthmic lysis", "#r#Radiolucent trace passing through the isthmus of " + nome_anat + "compatible with Isthmic lysis sequel.#r#"
                                                                                                                                              "#webvideo#https://youtu.be/gxmaMcpTs_o#webvideo#")

        sub_menu1 = wx.Menu("Vertebral body fracture")
        menu.Append(-1, sub_menu1.GetTitle(), sub_menu1)
        sub_menu1.Append(-1, "Fracture", "#r#Fracture of the vertebral body of " + nome_anat +".#r#"
                                                                                         "#webvideo#https://youtu.be/oISX1EBTiJM#webvideo#")
        sub_menu1.Append(-1, "with previous wedging.", "#r#Fracture of the vertebral body of " + nome_anat +"with previous wedging.#r#"
                                                                                                           "#webvideo#https://youtu.be/oISX1EBTiJM#webvideo#")
        sub_menu1.Append(-1, "with flattening.", "#r#Fracture of the vertebral body of " + nome_anat +"with flattening.#r#"
                                                                                                  "#webvideo#https://youtu.be/oISX1EBTiJM#webvideo#")
        menu.AppendSeparator()

        sub_menu3 = wx.Menu("Fracture of the thorny process")
        menu.Append(-1, sub_menu3.GetTitle(), sub_menu3)
        sub_menu3.Append(-1, "Fracture", "#r#Fracture of the thorny process of " + nome_anat +".#r#"
                                                                                            "#webvideo#https://youtu.be/oISX1EBTiJM#webvideo#")

        if nome_anat[0] != "C":
            menu.AppendSeparator()
            sub_menu2 = wx.Menu("Fratura do processo transverso")
            menu.Append(-1, sub_menu2.GetTitle(), sub_menu2)
            sub_menu2.Append(-1, "on the right", "#r#Fracture of the transverse process of " + nome_anat +" on right.#r#"
                                                                                                   "#webvideo#https://youtu.be/AJPQiu7-VWQ#webvideo#")
            sub_menu2.Append(-1, "on the left", "#r#Fracture of the transverse process of " + nome_anat +" on left.#r#"
                                                                                                    "#webvideo#https://youtu.be/AJPQiu7-VWQ#webvideo#")
            sub_menu2.Append(-1, "bilateral", "#r#Fracture of the transverse process of " + nome_anat +" bilateral.#r#"
                                                                                                   "#webvideo#https://youtu.be/AJPQiu7-VWQ#webvideo#")


        self.menu_coracao.AppendSeparator()
        menu = wx.Menu("Prótese discal")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Disc prosthesis", "#r#Disc prosthesis in #seleção_espaço_vertebral_sem_ponto_final# #descrever_integridade_material_livre#.#r#"
                                                                                                                                                                                                                                                                                 "#webvideo#https://youtu.be/dmO2BDDFigg#webvideo#")

        menu = wx.Menu("Metal fastening")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Posterior arthrodesis", "#r#Artrodese " + nome_anat_ex_lombar + " posterior transpedicular nos níveis dos corpos vertebrais #seleção_vertebra_sem_ponto#, composta por duas hastes e #num_parafuso_placa# parafusos de atenuação metálica, #descrever_integridade_material_livre#.#r#"
                                                                  "#bloquear_img#artrodese_e_cage_img.png#bloquear_img#"
                                                                  "#webvideo#https://youtu.be/Jl3ew3reRQA#webvideo#")
        menu.AppendSeparator()
        menu.Append(-1, "Anterior arthrodesis", "#r#arthrodesis " + nome_anat_ex_lombar + " anterior in the levels of the vertebral bodies #seleção_vertebra_sem_ponto#, composed of two rods and #num_parafuso_placa# metallic attenuation screws #descrever_integridade_material_livre#.#r#"
                                                                  "#bloquear_img#artrodese_e_cage_img.png#bloquear_img#"
                                                                  "#webvideo#https://youtu.be/Jl3ew3reRQA#webvideo#")





        menu.AppendSeparator()
        menu.Append(-1, "Intersomatic device (cage)", "#r#Intersomatic device (cage) in #seleção_espaço_vertebral# disc space.#r#"                                                                                                                                                                                                                                                                          
                                                            "#bloquear_img#artrodese_e_cage_img.png#bloquear_img#"
                                                            "#webvideo#https://youtu.be/f0D-t3qEhzQ#webvideo#")

        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


    def rx_normal(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="Radiography without particularities"):
        """Return customized button. must define
        the position by x and y."""

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0]+ nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0]+ nome_anat[1:])
        self.menu_coracao.AppendSeparator()
        self.menu_coracao.Append(-1, "Chest radiography without particularities.")
        self.menu_coracao.AppendSeparator()
        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat


# organ generico

    def organ_generico(self, x=1, y=1 ,largura=1 , altura=1, nome_anat ="organ", gen="o"):
        """Return customized button. must define
        the position by x and y."""

        style_plt = platebtn.PB_STYLE_NOBG
        self.plt_btn_anat = platebtn.PlateButton(self, label="", pos=(x, y), style=style_plt,
                                                 size=(largura, altura))
        img_check = wx.Image("xrd126.ipn", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.plt_btn_anat.SetToolTip(nome_anat.title()[0] + nome_anat[1:])
        self.plt_btn_anat.SetBackgroundColour("black")
        self.plt_btn_anat.SetPressColor(wx.LIGHT_GREY)
        self.menu_coracao = wx.Menu(nome_anat.title()[0] + nome_anat[1:])

        menu = wx.Menu("Integral structures.")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)
        menu.Append(-1, "Integral structures.")
        menu.Append(-1, "Conserved texture.")

        if "kidney" in nome_anat or "ureter" in nome_anat:
            menu = wx.Menu("Litíase")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Lithiase | small", "#r#Miniature radiopaque concretion projected on the " + nome_anat + ", which may correspond to " + nome_anat.split()[1].replace("kidney", "nephrolithiasis").replace("ureter", "ureterolithiasis") + ".#r#"
                                                                                                                                                                                                                                                               "#webvideo#https://youtu.be/XzNXhZ2aAI8#webvideo#")
            menu.Append(-1, "Lithiase | small | cm", "#r#Miniature radiopaque concretion projected on the topography of " + nome_anat + " measuring approximately --cm. It can correspond to " + nome_anat.split()[1].replace("kidney", "nephrolithiasis").replace("ureter", "ureterolithiasis") + ".#r#"
                                                                                                                                                                                                                                                                                                 "#webvideo#https://youtu.be/nt-cpZB_GfA#webvideo#")

        if nome_anat.split()[0] == "intestine":
            menu.Append(-1, "Normal distribution of gases and feces",
                        "#r#Normal distribution of gases and feces in intestinal loops.#r#"
                        "#webvideo#https://youtu.be/qXtREOCZw7U#webvideo#")
            menu.Append(-1, "Retroperitoneal lines | normal",
                        "#r#Partially outlined retroperitoneal lines and embroidery.#r#"
                        "#webvideo#https://youtu.be/qXtREOCZw7U#webvideo#")
            menu.Append(-1, "Absence of visible pathological calcification.", "#r#Absence of visible pathological calcification.#r#"
                                                                            "#webvideo#https://youtu.be/qXtREOCZw7U#webvideo#")
            menu.Append(-1, "Absence of renal or vesicular lithiasis",
                        "#r#Absence of images suggestive of renal or vesicular lithiasis.#r#"
                        "#webvideo#https://youtu.be/O7ypY-eoIFQ#webvideo#")
            menu.Append(-1, "Normal chest X-ray",
                        "#r#Absence of abnormality evidenced on chest radiography, especially absence of a sign of pneumoperitoneum.#r#"
                        "#webvideo#https://youtu.be/VfL7qKk25o0#webvideo#")
            menu.AppendSeparator()
            menu.Append(-1, "Normal radiological examination.", "#r#Normal radiological examination.#r#"
                                                         "#webvideo#https://youtu.be/qXtREOCZw7U#webvideo#")

            menu = wx.Menu("Distended intestinal loops")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "Distension of colic loops",
                        "#r#Distension of colic handles by accumulation of gases and fecal residues.#r#"
                        "#webvideo#https://youtu.be/pFliA4iBdBw#webvideo#")

            menu.Append(-1, "Diffuse Distension",
                        "#r#Diffuse distension of intestinal loops by fecal and gaseous content.#r#"
                        "#webvideo#https://youtu.be/mMLY1dmu9OY#webvideo#")

            menu.Append(-1, "Diffuse distension | coprostase",
                        "#r#Diffuse distension of intestinal loops by fecal and gaseous content, with signs of coprostase.#r#"
                        "#webvideo#https://youtu.be/oHCI65GugfI#webvideo#")

            menu = wx.Menu("Pneumoperitônio regiões ")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "subdiaphragmatic | hypocondriums.",
                        "#r#Moderate pneumoperitoneum observed in the sub-diaphragmatic regions, in the hypochondria.#r#"
                        "#webvideo#https://youtu.be/MkhKRt7XbPo#webvideo#")

            menu = wx.Menu("Materials | Findings")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "surgical clips | topography of the hypochondrium",
                        "#r#Linear materials are defined, with metallic attenuation, projected on the topography of the right hypochondrium, which may correspond to surgical clips. Correlate to the antecedents.#r#"
                        "#webvideo#https://youtu.be/qNEbypney3w#webvideo#")


        menu = wx.Menu("Type of radiographic study\tMenu")
        self.menu_coracao.Append(-1, menu.GetTitle(), menu)

        submenu1 = wx.Menu("Evaluation")
        menu.Append(-1, submenu1.GetTitle(), submenu1)
        submenu1.Append(-1, "post-traumatic", "#r#Post-traumatic radiographic study, which must be related to the patient's clinical data and background.#r#")
        submenu1.Append(-1, "post-surgical", "#r#Post-surgical radiographic study, which must be related to the clinical-surgical data and the patient's history.#r#")
        menu.AppendSeparator()
        submenu2 = wx.Menu("Control study")
        menu.Append(-1, submenu2.GetTitle(), submenu2)
        submenu2.Append(-1, "evolutionary | correlate", "#r#Radiographic evolutionary control study that must be related to clinical data and previous exams.#r#")
        submenu2.Append(-1, "evolutionary | evidence:", "#r#Radiographic evolutionary control study shows:#r#")
        submenu2.AppendSeparator()
        submenu2.Append(-1, "post-traumatic", "#r#Radiographic study of post-traumatic evolutionary control, which must be correlated to the patient's clinical data and background.#r#")
        submenu2.Append(-1, "post-surgical", "#r#Radiographic study of post-surgical evolutionary control, which must be correlated to the clinical-surgical data and the patient's history.#r#")

        if "uterus" in nome_anat:
            menu = wx.Menu("Medical supplies")
            self.menu_coracao.Append(-1, menu.GetTitle(), menu)
            menu.Append(-1, "There is metallic opacity material in the topography of the uterus corresponding to an intrauterine device.",
                        "#r#Metallic opacity material is observed in the topography of the uterus corresponding to IUDs.#r#"
                        "#webvideo#https://youtu.be/10R0FfaFXx4#webvideo#")



        self.plt_btn_anat.SetMenu(self.menu_coracao)
        return self.plt_btn_anat
