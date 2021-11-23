import streamlit as st
import py_avataaars as pa
import os
from PIL import Image
import base64
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title='Avatar Generator',page_icon='👽')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
	content:'Made with ❤️ by om pramod'; 
	visibility: visible ;
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def load_lottiefile(filepath: str):
        with open(filepath, "r") as f :
            return json.load(f)

lottie_coding = load_lottiefile("avatar.json")

st_lottie(
        lottie_coding,
        speed= 1,
        reverse=False,
        loop=True,
        height=190,
        width= 700,
        key=None
    )

st.markdown("<h1 style='text-align: center; color:blue ;font-family: fantasy'>AVATAR MAKER</h1>", unsafe_allow_html=True)
st.markdown("*****")
st.success("*Welcome to Avatar Maker! This app allows you to build your own custom avatars based on modular templates provided herein. Cartoonify yourself hassle free. Replace your photo on social media sites, forums or chat programs with your own created cartoon avatar.*")
st.markdown("****")
st.sidebar.header('Customize your avatar')

option_style = st.sidebar.selectbox('Style', ('CIRCLE', 'TRANSPARENT'))

list_skin_color = ['TANNED','YELLOW','PALE','LIGHT','BROWN','DARK_BROWN','BLACK']
list_top_type = ['NO_HAIR','EYE_PATCH','HAT','HIJAB','TURBAN',
                 'WINTER_HAT1','WINTER_HAT2','WINTER_HAT3',
                 'WINTER_HAT4','LONG_HAIR_BIG_HAIR','LONG_HAIR_BOB',
                 'LONG_HAIR_BUN','LONG_HAIR_CURLY','LONG_HAIR_CURVY',
                 'LONG_HAIR_DREADS','LONG_HAIR_FRIDA','LONG_HAIR_FRO',
                 'LONG_HAIR_FRO_BAND','LONG_HAIR_NOT_TOO_LONG',
                 'LONG_HAIR_SHAVED_SIDES','LONG_HAIR_MIA_WALLACE',
                 'LONG_HAIR_STRAIGHT','LONG_HAIR_STRAIGHT2',
                 'LONG_HAIR_STRAIGHT_STRAND','SHORT_HAIR_DREADS_01',
                 'SHORT_HAIR_DREADS_02','SHORT_HAIR_FRIZZLE',
                 'SHORT_HAIR_SHAGGY_MULLET','SHORT_HAIR_SHORT_CURLY',
                 'SHORT_HAIR_SHORT_FLAT','SHORT_HAIR_SHORT_ROUND',
                 'SHORT_HAIR_SHORT_WAVED','SHORT_HAIR_SIDES',
                 'SHORT_HAIR_THE_CAESAR','SHORT_HAIR_THE_CAESAR_SIDE_PART']
list_hair_color = ['AUBURN','BLACK','BLONDE','BLONDE_GOLDEN','BROWN',
                   'BROWN_DARK','PASTEL_PINK','PLATINUM','RED','SILVER_GRAY']
list_hat_color = ['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02',
                  'HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE',
                  'PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']

list_facial_hair_type = ['DEFAULT','BEARD_MEDIUM','BEARD_LIGHT','BEARD_MAJESTIC','MOUSTACHE_FANCY','MOUSTACHE_MAGNUM']
list_facial_hair_color = ['AUBURN','BLACK','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PLATINUM','RED']
list_mouth_type = ['DEFAULT','CONCERNED','DISBELIEF','EATING','GRIMACE','SAD','SCREAM_OPEN','SERIOUS','SMILE','TONGUE','TWINKLE','VOMIT']
list_eye_type = ['DEFAULT','CLOSE','CRY','DIZZY','EYE_ROLL','HAPPY','HEARTS','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
list_eyebrow_type = ['DEFAULT','DEFAULT_NATURAL','ANGRY','ANGRY_NATURAL','FLAT_NATURAL','RAISED_EXCITED','RAISED_EXCITED_NATURAL','SAD_CONCERNED','SAD_CONCERNED_NATURAL','UNI_BROW_NATURAL','UP_DOWN','UP_DOWN_NATURAL','FROWN_NATURAL']
list_accessories_type = ['DEFAULT','KURT','PRESCRIPTION_01','PRESCRIPTION_02','ROUND','SUNGLASSES','WAYFARERS']
list_clothe_type = ['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
list_clothe_color = ['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
list_clothe_graphic_type = ['BAT','CUMBIA','DEER','DIAMOND','HOLA','PIZZA','RESIST','SELENA','BEAR','SKULL_OUTLINE','SKULL']

option_skin_color = st.sidebar.selectbox('Skin color',
                                         list_skin_color,
                                         )

st.sidebar.subheader('Head top')
option_top_type = st.sidebar.selectbox('Head top',
                                        list_top_type,
                                        )
option_hair_color = st.sidebar.selectbox('Hair color',
                                         list_hair_color,
                                         )
option_hat_color = st.sidebar.selectbox('Hat color',
                                         list_hat_color,
                                         )

st.sidebar.subheader('Face')
option_facial_hair_type = st.sidebar.selectbox('Facial hair type',
                                                list_facial_hair_type,
                                                )
option_facial_hair_color = st.sidebar.selectbox('Facial hair color',
                                                list_facial_hair_color,
                                                )
option_mouth_type = st.sidebar.selectbox('Mouth type',
                                          list_mouth_type,
                                          )
option_eye_type = st.sidebar.selectbox('Eye type',
                                        list_eye_type,
                                        )
option_eyebrow_type = st.sidebar.selectbox('Eyebrow type',
                                            list_eyebrow_type,
                                            )

st.sidebar.subheader('Clothe and accessories')
option_accessories_type = st.sidebar.selectbox('Accessories type',
                                                list_accessories_type,
                                                )
option_clothe_type = st.sidebar.selectbox('Clothe type',
                                           list_clothe_type,
                                           )
option_clothe_color = st.sidebar.selectbox('Clothe Color',
                                            list_clothe_color,
                                            )
option_clothe_graphic_type = st.sidebar.selectbox('Clothe graphic type',
                                                   list_clothe_graphic_type,
                                                   )

avatar = pa.PyAvataaar(
        #style=pa.AvatarStyle.CIRCLE,
        style=eval('pa.AvatarStyle.%s' % option_style),
        skin_color=eval('pa.SkinColor.%s' % option_skin_color),
        top_type=eval('pa.TopType.SHORT_HAIR_SHORT_FLAT.%s' % option_top_type),
        hair_color=eval('pa.HairColor.%s' % option_hair_color),
        hat_color=eval('pa.Color.%s' % option_hat_color),
        facial_hair_type=eval('pa.FacialHairType.%s' % option_facial_hair_type),
        facial_hair_color=eval('pa.HairColor.%s' % option_facial_hair_color),
        mouth_type=eval('pa.MouthType.%s' % option_mouth_type),
        eye_type=eval('pa.EyesType.%s' % option_eye_type),
        eyebrow_type=eval('pa.EyebrowType.%s' % option_eyebrow_type),
        nose_type=pa.NoseType.DEFAULT,
        accessories_type=eval('pa.AccessoriesType.%s' % option_accessories_type),
        clothe_type=eval('pa.ClotheType.%s' % option_clothe_type),
        clothe_color=eval('pa.Color.%s' % option_clothe_color),
        clothe_graphic_type=eval('pa.ClotheGraphicType.%s' %option_clothe_graphic_type)
    )

# Custom function for encoding and downloading avatar image
def imagedownload(filename):
    image_file = open(filename, 'rb')
    b64 = base64.b64encode(image_file.read()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:image/png;base64,{b64}" download={filename}>Download {filename} File</a>'
    return href

st.subheader('**Your Rendered Avatar**')
rendered_avatar = avatar.render_png_file('avatar.png')
image = Image.open('avatar.png')
st.image(image)
st.markdown(imagedownload('avatar.png'), unsafe_allow_html=True)
