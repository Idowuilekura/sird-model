import streamlit as st
import matplotlib.pyplot as plt
import simulate

page_bg_img = '''
<style>
.stApp {
    background-image: url("https://unsplash.com/photos/_ts3NfjvaXo");
    background-size: cover;
    position: absolute;
    top: 0px;
    right: 0px;
    bottom: 0px;
    left: 0px;
    background-color: rgba(0,0,0,0.25);

}
footer {
    visibility: hidden;
}

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: grey;
    color: black;
    text-align: center;
}

</style>
<div class ="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/ilekuraidowu/" target="_blank">Idowu Ilekura</a></p>
</div>
'''

st.markdown(page_bg_img,unsafe_allow_html=True)

header = st.beta_container()

simulation = st.beta_container()

with header:
    st.title('Welcome to Konvid-18 simulation')

    st.text('\
        This is a fictional simulation of a disease called Konvid-18')


# st.subheader('Simulating Disease')

# st.sidebar.subheader('Simulation Options')
# st.text(\
#     'total population is the total number of residents in the community')
#Sidebar Options:

with simulation:
    st.subheader('Time to simulate Disease'
    )
    st.text("\
        Here you get to choose the simulation parameters")
    sel_col,okay  = st.beta_columns(2)

    
    total_population = sel_col.number_input('\
        Enter the total number of people residing\
             in the community below')
    num_infected = sel_col.number_input('\
        Enter the total number of infected people below')
    num_immuned = sel_col.number_input('\
        Enter the total number of immuned people\
            below')
    num_dead = sel_col.number_input('\
        Enter the total number of dead people below')
    
    sim_days = sel_col.number_input("\
        Enter the number of days to be simulated\
            Enter just as a number")

    contact_rate = sel_col.slider("\
        What do you think the contact rate shoulb be?",min_value= 0.1,max_value=0.7,step=0.01)
    
    recovery_rate = sel_col.slider("\
        What do you think the recovery rate should be?",min_value=0.01,max_value=0.1,step=0.005)

    death_rate = sel_col.slider('\
        What do you think the death rate should be?',min_value=0.01,max_value=0.07,step=0.001)

    
    btn = sel_col.button('simulate')

    def simulate_and_plot():
        simulate.simulate_disease(\
            int(total_population),\
                int(num_infected),
                    int(num_immuned),int(num_dead),\
                        contact_rate,recovery_rate,death_rate,\
                            int(sim_days))

    if btn:
        simulate_and_plot()
    else:
        pass


