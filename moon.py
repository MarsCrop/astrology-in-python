#!/usr/bin/env/ python3
import datetime
import ephem

today = datetime.date.today()

def get_phase_on_day(year,month,day):
  """Returns a floating-point number from 0-1. where 0=new, 0.25 = first_quarter, 0.5=full, 0.75 = last_quarter, 1=new"""

  date=ephem.Date(datetime.date(year,month,day))

  nnm = ephem.next_new_moon(date)
  pnm = ephem.previous_new_moon(date)

  lunation=(date-pnm)/(nnm-pnm)

  return lunation

def get_moons_in_year(year, month, day):
  """Returns a list of the full moons, first quarter moons, last quarter moons and new moons in a year."""
  moons=[]

  date=ephem.Date(datetime.date(year,month,day))
  while date.datetime().year==year:
    date=ephem.next_full_moon(date)
    moons.append((date,'Luna Llena'))

  date=ephem.Date(datetime.date(year,month,day))
  while date.datetime().year==year:
    date=ephem.next_first_quarter_moon(date)
    moons.append((date,'Cuarto Creciente'))

  date=ephem.Date(datetime.date(year,month,day))
  while date.datetime().year==year:
    date=ephem.next_last_quarter_moon(date)
    moons.append((date,'Cuarto Menguante'))

  date=ephem.Date(datetime.date(year,month,day))
  while date.datetime().year==year:
    date=ephem.next_new_moon(date)
    moons.append((date,'Luna Nueva'))

  moons_sorted = sorted(moons, key = lambda x: x[0].datetime())

  moons_in_year = []

  for i in moons_sorted: 
        moons_in_year.append((i[0].datetime().ctime(), i[1]))

  return moons_in_year

print (get_phase_on_day(today.year, today.month, today.day))

print (get_moons_in_year(today.year, today.month, today.day))
