# Base Class Documentation

### Member Variables:
* calls as List of Dictionaries

<br />
calls is a List of Dictionaries<br />
Example Dictionary:<br />
{<br />
&emsp;"city_name": in str<br />
&emsp;"time": in hh-mm-ss<br />
&emsp;"date": in dd-mm-yyyy<br />
&emsp;"temp": celsius in int<br />
&emsp;"humidity": in percent in float from 0 - 1<br />
&emsp;"description": a short description about the weather in str<br />
&emsp;"plz": city id in str<br />
}<br />
<br />

### How to implement
from BaseClassAPI import BaseClassAPI

class ExampleAPI(BaseClassAPI): <br />
&emsp;def getWeather(self): <br />
&emsp;&emsp;# own implementation
