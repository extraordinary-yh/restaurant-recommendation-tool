#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    import pyswip
except ImportError:
    get_ipython().system('pip install pyswip')
    import pyswip

KB = """
%  Tell prolog that known/3 and multivalued/1 will be added later
:- dynamic known/3, multivalued/1.




% Enter your KB below this line:

restaurant(casa_munay) :- cuisine(local), diet(vegetarian), activity(none), distance(walking_distance), number_of_people(maximum_6_are_going), budget(im_broke), atmosphere(vibrant), outdoor_sitting(yes).

restaurant(mumbai) :- cuisine(desi), diet(omnivore), activity(none), distance(walking_distance), number_of_people(unsure), budget(surviving), atmosphere(quiet), outdoor_sitting(no).

restaurant(namida) :- diet(vegan), activity(none), distance(willing_take_a_car), number_of_people(unsure), budget(surviving), atmosphere(vibrant), outdoor_sitting(no).

restaurant(la_pescadorita) :- cuisine(mediterrenean), diet(pescaterian), activity(football), distance(walking_distance), number_of_people(unsure), budget(im_broke), atmosphere(vibrant), outdoor_sitting(yes).

restaurant(cantina_sunae) :- cuisine(asian), diet(vegan), activity(none), distance(willing_take_a_car), number_of_people(maximum_6_are_going), budget(surviving), atmosphere(quiet), outdoor_sitting(no).

restaurant(tora) :- cuisine(asian), diet(vegan), activity(none), distance(willing_take_a_car), number_of_people(well_I_need_room_for_upto_15), budget(surviving), atmosphere(vibrant), outdoor_sitting(no).

restaurant(al_rawshe) :- cuisine(lebanese), diet(halal), activity(none), distance(willing_take_a_car), number_of_people(well_I_need_room_for_upto_15), budget(surviving), atmosphere(vibrant), outdoor_sitting(no).

restaurant(carbenet) :- cuisine(local), diet(omnivore), activity(none), distance(walking_distance), number_of_people(unsure), budget(just_got_paid), atmosphere(quiet), outdoor_sitting(no).

restaurant(dogg) :- cuisine(fastfood), diet(omnivore), activity(music), distance(walking_distance), number_of_people(well_I_need_room_for_upto_15), budget(surviving), atmosphere(vibrant), outdoor_sitting(yes).

restaurant(gardiner) :- cuisine(local), diet(omnivore), activity(music), distance(willing_take_a_car), number_of_people(well_I_need_room_for_upto_15), budget(just_got_paid), atmosphere(quiet), outdoor_sitting(no).

restaurant(dostana) :- cuisine(desi), diet(omnivore), activity(none), distance(walking_distance), number_of_people(unsure), budget(surviving), atmosphere(vibrant), outdoor_sitting(no).

restaurant(gibraltar) :- cuisine(fastfood), diet(omnivore), activity(football), distance(willing_take_a_car), number_of_people(well_I_need_room_for_upto_15), budget(surviving), atmosphere(vibrant), outdoor_sitting(no).

restaurant(sugar) :- cuisine(fastfood), diet(omnivore), activity(football), distance(willing_take_a_car), number_of_people(well_I_need_room_for_upto_15), budget(im_broke), atmosphere(vibrant), outdoor_sitting(no).

restaurant(thelonius) :- cuisine(local), diet(omnivore), activity(jazz), distance(willing_take_a_car), number_of_people(well_I_need_room_for_upto_15), budget(surviving), atmosphere(vibrant), outdoor_sitting(no).

% The code below implements the prompting to ask the user:

cuisine(X) :- menuask(cuisine, X, [local, desi, mediterrenean, asian, lebanese, fastfood]).
diet(X) :- menuask(diet, X, [vegetarian, omnivore, pescaterian, vegan, halal]).
activity(X) :- menuask(activity, X, [none, football, music, jazz]).
distance(X) :- menuask(distance, X, [walking_distance, willing_take_a_car]).
number_of_people(X) :- menuask(number_of_people, X, [maximum_6_are_going, well_I_need_room_for_upto_15, unsure]).
budget(X) :- menuask(budget, X, [im_broke, surviving, just_got_paid]).
atmosphere(X) :- menuask(atmosphere, X, [vibrant, quiet]).
outdoor_sitting(X) :- menuask(outdoor_sitting, X, [yes, no]).



menuask(A, V, Menu) :- 
known(yes, A, V), !.


menuask(A, V, Menu) :-
known(yes, A, _), !, fail.


menuask(A, V, Menu) :- 
known(yes, A, V), V \== Val, !, fail.

% % Making the menu ask
menuask(A, V, Menu) :- 
    %write_py(Menu), nl,
    read_py(A, Ans, Menu),
    check_val(Ans, A, V, Menu),
    asserta(known(yes, A, Ans)),
    Ans == V.

check_val(Ans, _, _, Menu) :- member(Ans, Menu), !.
check_val(Ans, A, V, Menu) :- 
    write_py(Ans), write_py(' is not a known answer, please try again.'), nl,
    menuask(A, V, Menu).



"""

