from tkinter import *
from tkinter.ttk import *

us = ['Gianmarco', 'X', 'Y', 'Z', 'W']

#data from January, for the whole 2020 month by month
month_average_sourced = [12.37, 11.57, 14.11, 19.63, 14.62, 13.36, 12.12, 15.27, 16.18, 15.96, 17.90]
month_average_contacted = [11.05, 15.09, 12.95, 12.06, 11.32, 12.89, 19.20, 17.25, 14.76, 17.99, 16.48]
average_attendancy = [84.52, 87.50, 95.45, 88.09, 96.25, 89.29, 73.91, 70.47, 89.09, 93.64, 83.81]

window = Tk()

window.geometry('700x520')

window.configure(background='white')

window.title("KPI by Gianmarco Ercolani")

lbl = Label(window, text="Month analysed:", width= 20)

lbl.configure(background='white')

lbl.grid(column=0, row=0, padx=25, pady=(25, 45))

currentmonth = Combobox(window)

currentmonth ['values']= ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

currentmonth.current(0)

currentmonth.grid(column=1, row=0, padx=25, pady=(25, 45))

lbl = Label(window, text=f"{us[0]} Sourced    ", width=20)

lbl.grid(column=0, row=2, padx=5, pady=5)

lbl.configure(background='white')

sourcedm = Entry(window,width=10)

sourcedm.grid(column=1, row=2)

sourcedmansw = sourcedm.get()

lbl = Label(window, text=f"{us[0]} Contacted    ", width=20)

lbl.grid(column=0, row=3, padx=5, pady=5)

lbl.configure(background='white')

contactedm = Entry(window,width=10)

contactedm.grid(column=1, row=3)

contactedmansw = contactedm.get()

lbl = Label(window, text="In how many days?    ", width=20)

lbl.grid(column=0, row=4, padx=5, pady=5)

lbl.configure(background='white')

daysm = Entry(window,width=10)

daysm.grid(column=1, row=4)

daysmansw = daysm.get()

lbl = Label(window, text=f"{us[1]} Sourced    ", width=25)

lbl.grid(column=3, row=2)

lbl.configure(background='white')

sourcedo = Entry(window,width=10)

sourcedo.grid(column=4, row=2)

sourcedoansw = sourcedo.get()

lbl = Label(window, text=f"{us[1]} Contacted    ", width=25)

lbl.grid(column=3, row=3)

lbl.configure(background='white')

contactedo = Entry(window,width=10)

contactedo.grid(column=4, row=3)

contactedoansw = contactedo.get()

lbl = Label(window, text="In how many days?    ", width=25)

lbl.grid(column=3, row=4)

lbl.configure(background='white')

dayso = Entry(window,width=10)

dayso.grid(column=4, row=4)

daysoansw = dayso.get()

lbl = Label(window, text=f"{us[2]} Sourced    ", width=20)

lbl.grid(column=0, row=6, padx=5, pady=(35, 5))

lbl.configure(background='white')

sourceds = Entry(window,width=10)

sourceds.grid(column=1, row=6, pady=(35, 5))

sourcedsansw = sourceds.get()

lbl = Label(window, text=f"{us[2]} Contacted    ", width=20)

lbl.grid(column=0, row=7, padx=5, pady=5)

lbl.configure(background='white')

contacteds = Entry(window,width=10)

contacteds.grid(column=1, row=7)

contactesmansw = contacteds.get()

lbl = Label(window, text="In how many days?    ", width=20)

lbl.grid(column=0, row=8, padx=5, pady=5)

lbl.configure(background='white')

dayss = Entry(window,width=10)

dayss.grid(column=1, row=8)

dayssansw = dayss.get()

lbl = Label(window, text=f"{us[3]} Sourced    ", width=25)

lbl.grid(column=3, row=6, pady=(35, 5))

lbl.configure(background='white')

sourcedd = Entry(window,width=10)

sourcedd.grid(column=4, row=6, pady=(35, 5))

sourceddansw = sourcedd.get()

lbl = Label(window, text=f"{us[3]} Contacted    ", width=25)

lbl.grid(column=3, row=7)

lbl.configure(background='white')

contactedd = Entry(window,width=10)

contactedd.grid(column=4, row=7)

contacteddansw = contactedd.get()

lbl = Label(window, text="In how many days?    ", width=25)

lbl.grid(column=3, row=8)

lbl.configure(background='white')

daysd = Entry(window,width=10)

daysd.grid(column=4, row=8)

daysdansw = daysd.get()

lbl = Label(window, text=f"{us[4]} Sourced    ", width=20)

lbl.grid(column=0, row=9, padx=5, pady=(35,5))

lbl.configure(background='white')

sourcedg = Entry(window,width=10)

sourcedg.grid(column=1, row=9, pady=(35, 5))

sourcedgansw = sourcedg.get()

lbl = Label(window, text=f"{us[4]} Contacted    ", width=20)

lbl.grid(column=0, row=10, padx=5, pady=5)

lbl.configure(background='white')

contactedg = Entry(window,width=10)

contactedg.grid(column=1, row=10)

contactedgansw = contactedg.get()

lbl = Label(window, text="In how many days?    ", width=20)

lbl.grid(column=0, row=11, padx=5, pady=5)

lbl.configure(background='white')

daysg = Entry(window,width=10)

daysg.grid(column=1, row=11)

daysgansw = daysm.get()

def result():

    monthansw = currentmonth.current()

    length = len(us)

    result = Tk()

    result.geometry('360x395')

    result.configure(background='white')

    result.title("Results by Gianmarco Ercolani")

    intsourcedm = int(sourcedm.get())
    intcontactedm = int(contactedm.get())
    intdaysm = int(daysm.get())

    intsourcedo = int(sourcedo.get())
    intcontactedo = int(contactedo.get())
    intdayso = int(dayso.get())

    intsourceds = int(sourceds.get())
    intcontacteds = int(contacteds.get())
    intdayss = int(dayss.get())

    intsourcedd = int(sourcedd.get())
    intcontactedd = int(contactedd.get())
    intdaysd = int(daysd.get())

    intsourcedg = int(sourcedg.get())
    intcontactedg = int(contactedg.get())
    intdaysg = int(daysg.get())

    averagesm = intsourcedm/intdaysm
    averagecm = intcontactedm/intdaysm

    averageso = intsourcedo/intdayso
    averageco = intcontactedo/intdayso

    averagess = intsourceds/intdayss
    averagecs = intcontacteds/intdayss

    averagesd = intsourcedd/intdaysd
    averagecd = intcontactedd/intdaysd

    averagesg = intsourcedg/intdaysg
    averagecg = intcontactedg/intdaysg

    lbl = Label(result, text=(f"{us[0]} sourced (daily average): " "{:.2f}".format(averagesm)), width=60)
    lbl.configure(background='white')
    lbl.grid(column=0, row=0, pady=(10, 0))
    lbl = Label(result, text=(f"{us[0]} contacted (daily average): " "{:.2f}\n".format(averagecm)), width=60)
    lbl.configure(background='white')
    lbl.grid(column=0, row=1)
    lbl = Label(result, text=(f"{us[1]} sourced (daily average): " "{:.2f}".format(averageso)), width=60)
    lbl.grid(column=0, row=2)
    lbl = Label(result, text=(f"{us[1]} contacted (daily average): " "{:.2f}\n".format(averageco)), width=60)
    lbl.grid(column=0, row=3)
    lbl = Label(result, text=(f"{us[2]} sourced (daily average): " "{:.2f}".format(averagess)), width=60)
    lbl.configure(background='white')
    lbl.grid(column=0, row=4)
    lbl = Label(result, text=(f"{us[2]} contacted (daily average): " "{:.2f}\n".format(averagecs)), width=60)
    lbl.configure(background='white')
    lbl.grid(column=0, row=5)
    lbl = Label(result, text=(f"{us[3]} sourced (daily average): " "{:.2f}".format(averagesd)), width=60)
    lbl.grid(column=0, row=6)
    lbl = Label(result, text=(f"{us[3]} contacted (daily average): " "{:.2f}\n".format(averagecd)), width=60)
    lbl.grid(column=0, row=7)
    lbl = Label(result, text=(f"{us[4]} sourced (daily average): " "{:.2f}".format(averagesg)), width=60)
    lbl.configure(background='white')
    lbl.grid(column=0, row=8)
    lbl = Label(result, text=(f"{us[4]} contacted (daily average): " "{:.2f}\n".format(averagecg)), width=60)
    lbl.configure(background='white')
    lbl.grid(column=0, row=9, pady=(0, 12))

    averagesteam = (averagesm + averageso + averagess + averagesd + averagesg) / length
    averagecteam = (averagecm + averageco + averagecs + averagecd + averagecg) / length

    month_average_sourced.append(averagesteam)
    month_average_contacted.append(averagecteam)

    lbl = Label(result, text=(f"Team sourced candidates (daily average): " "{:.2f}".format(averagesteam)), width=60)
    lbl.grid(column=0, row=10)
    lbl = Label(result, text=(f"Team contacted candidates (daily average): " "{:.2f}\n".format(averagecteam)), width=60)
    lbl.grid(column=0, row=11)

    month_forecast = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

    lbl = Label(result, text=(f"Forecast team sourced candidates for {month_forecast[monthansw+1]} (per week): " "{:.2f}".format((sum(month_average_sourced)/len(month_average_sourced)) * 5 * length * (average_attendancy[monthansw + 1]/100))), width=60)
    lbl.configure(background='white')
    lbl.grid(column=0, row=12)
    lbl = Label(result, text=(f"Forecast team contacted candidates for {month_forecast[monthansw+1]} (per week): " "{:.2f}".format((sum(month_average_contacted)/len(month_average_contacted)) * 5 * length * (average_attendancy[monthansw + 1]/100))) , width=60)
    lbl.configure(background='white')
    lbl.grid(column=0, row=13)

    result.mainloop()

w = Button(window, text ="Let's go!", command=result)

w.place(relx="0.43",rely="0.87")

window.mainloop()
