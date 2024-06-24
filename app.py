import streamlit as st
from streamlit_folium import st_folium
import folium
from utils import property_type_formatter, calculate_distance, predict, get_city_name

if 'selected_point' not in st.session_state:
    st.session_state.selected_point = [-37.805443949342724, 144.97558593750003]

if 'zoom_level' not in st.session_state:
    st.session_state.zoom_level = 10

def create_map(selected_point, zoom_level):
    m = folium.Map(location=selected_point, zoom_start=zoom_level)
    folium.Marker(selected_point, tooltip="Selected Point").add_to(m)
    return m

@st.experimental_dialog("Application Error!")
def application_error(error_message):
    st.markdown(error_message)

@st.experimental_dialog("Predicted Property Value")
def prediction_popup(error_message):
    st.markdown(error_message)

st.markdown("##### Select Property Location")
map_object = create_map(st.session_state.selected_point, st.session_state.zoom_level)
last_click = st_folium(map_object, width=700, height=500)

if last_click is not None:
    last_clicked = last_click.get('last_clicked', None)
    map_center = last_click.get('center', None)
    zoom_level = last_click.get('zoom', None)
    
    if last_clicked is not None and map_center is not None and zoom_level is not None:
        lat = last_clicked.get('lat', None)
        lng = last_clicked.get('lng', None)
        if lat is not None and lng is not None:
            st.session_state.selected_point = [lat, lng]
            st.session_state.zoom_level = zoom_level
            st.rerun()
            
with st.form("main-form", clear_on_submit=False, border=False):
    
    st.markdown("##### Land Size")
    land_size = st.slider(label="Land Size",
                          min_value=55.0,
                          max_value=10000.0,
                          step=0.1,
                          label_visibility="collapsed")
    
    st.markdown("##### Number of Rooms")
    num_rooms = st.slider(label="Rooms",
                          min_value=1,
                          max_value=12,
                          step=1,
                          label_visibility="collapsed")
    
    st.markdown("##### Number of Bedrooms")
    num_bed_rooms = st.slider(label="Bedrooms",
                          min_value=0,
                          max_value=12,
                          step=1,
                          label_visibility="collapsed")
    
    st.markdown("##### Number of Bathrooms")
    num_bath_rooms = st.slider(label="Bathrooms",
                          min_value=1,
                          max_value=9,
                          step=1,
                          label_visibility="collapsed")
    
    st.markdown("##### Property Type")
    property_type = st.selectbox(label="Property Type",
                                 options = ["h", "u", "t"],
                                 index=None,
                                 format_func=property_type_formatter,
                                 label_visibility="collapsed")
    
    
    submit = st.form_submit_button()
    
    if submit:
        clicked_point = (st.session_state.selected_point[0], st.session_state.selected_point[1])
        
        latitude = clicked_point[0]
        longitude = clicked_point[1]
        
        city_name, country_name = get_city_name(latitude, longitude)
        
        if (city_name.lower() == "melbourne") and (country_name.lower() == "australia"):
        
            distance = calculate_distance(clicked_point)
            
            bed2bath = num_bed_rooms / num_bath_rooms
            
            submitted_data = {
                "Distance": distance,
                "Landsize": land_size,
                "Lattitude": latitude,
                "Longtitude": longitude,
                "BedtoBath": bed2bath,
                "Rooms": num_rooms,
                "Type": property_type,
                "Bedroom2": num_bed_rooms,
                "Bathroom": num_bath_rooms,
            }
            
            prediction = predict(submitted_data)
            prediction_popup(f"Predicted Property Value - `A$ {prediction}`")
            
        else:
            application_error(f"Please select a location in `Melbourne`, `Australia`. But given `{city_name}`, `{country_name}`")