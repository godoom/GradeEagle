# GradeEagle


you will have to import all that stuff, and if it complains it will probably tell you what you need to pip install for it
</br>

line 19 and 20 is where i open the csv files, one of them is conors one of them is Leo and Dannys. conor should probably make </br>
sure that his csv file is the same as leo and dannys so we can just all pull from a single file </br>

lines 23 through 161 are conors code, lines 142 and 156 are where the figures that will be used in the front end are actually declare </br>
line 239 for leos figure (bar) </br>
line 187 for dannys figure (scatter) </br>

also if you compare lines 48-54(conors filter variables) to lines 175-178 (leos and dannys variables, i harded coded these for our standup) </br>
you can see that the names and the way that they are created are different. so conor should probably change his to match leo and dannys. </br>

then if everyone is using the filter variables on lines 175-178, we can easily have some filter buttons on the front end to toggle </br>

line 259 to 280 is pretty much the front end. this video describes it: https://www.youtube.com/watch?v=e4ti2fCpXMI&t=214s . Basicaly you just put whatever compenents in that you want. </br>
this where we need to add the filter buttons and somehow tie these buttons to our filter variables so the graphs can update. </br>

line 284 is the callback code that updates the graph when the dropdown value is changed. probably gonna have do something here too</br>
with our filter buttons
