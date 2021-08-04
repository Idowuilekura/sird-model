import matplotlib.pyplot as plt
import streamlit as st

def simulate_disease(total_population,num_infected,num_immuned,num_dead,contact_rate=0.5,recovery_rate=0.035,death_rate = 0.005,sim_days=500):
    """function the simulate Konvid-18 disease
    """
    fig = plt.figure()
    total_population = total_population
    num_susceptible = total_population - num_infected
    num_infected = num_infected
    num_dead = num_dead
    num_immuned = num_immuned
    sim_days = sim_days
    susceptible_list = [total_population]
    infected_list = [num_infected]
    immuned_list = [num_immuned]
    dead_list = [num_dead]
    contact_rate = contact_rate
    recovery_rate = recovery_rate
    death_rate = death_rate 
    
    for day in range(1,sim_days):
        num_infected_daily = (contact_rate * num_infected * num_susceptible)/total_population
        num_immuned_daily = recovery_rate * num_infected
        num_dead_daily = death_rate * num_infected 
        num_infected = num_infected+ (num_infected_daily -num_immuned_daily -num_dead_daily)
        num_susceptible = num_susceptible - num_infected_daily
        num_immuned += num_immuned_daily
        num_dead += num_dead_daily
        
        susceptible_list.append(num_susceptible)
        infected_list.append(num_infected)
        immuned_list.append(num_immuned)
        dead_list.append(num_dead)

    plt.plot(\
        range(0,sim_days),susceptible_list,color='green',label="Susceptibles")
    plt.plot(\
        range(0,sim_days),infected_list,color="red",label='Infected')
    plt.plot(\
        range(0,sim_days),immuned_list,'blue',label='Immuned')
    plt.plot(\
        range(0,sim_days),dead_list,color='orange',label='Dead')

    plt.title('Konvid-18 Simulation')
    plt.legend()
    st.pyplot(fig)

    