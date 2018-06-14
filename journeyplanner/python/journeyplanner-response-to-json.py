# Licensed under the EUPL, Version 1.2 or – as soon they will be approved by
# the European Commission - subsequent versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at:
#
#   https://joinup.ec.europa.eu/software/page/eupl
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Licence is distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Licence for the specific language governing permissions and
# limitations under the Licence.

import json
import socket
import os
from six.moves import urllib

# This file provides an example for calling the journeyplanner API from Python and saving the response in a file
# Please change values for ET-Client-Name and User-Agent to values that identify you, before you run this example

HEADERS = {'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'python-code-example-' + socket.gethostname(),
            'ET-Client-Name': 'python-code-example-' + socket.gethostname(),
            'ET-Client-ID': socket.gethostname()}

GRAPHQL_ENDPOINT = "https://api.entur.org/journeyplanner/2.0/index/graphql"
CONNECT_TIMEOUT_SECONDS = 15

print("About to execute a graphql call to Enturs journeyplanner API")

def sendGraphqlQuery(query, variables):
    data = {'query': query, 'variables': variables}

    req = urllib.request.Request(GRAPHQL_ENDPOINT, json.dumps(data).encode('utf-8'), HEADERS)

    response = urllib.request.urlopen(req, timeout=CONNECT_TIMEOUT_SECONDS)
    return response.read().decode('utf-8')

query = """
    {
    stopPlace(id: "NSR:StopPlace:58282") {
        name
        quays {
                day: estimatedCalls(startTime: "2018-06-08T07:00:00+0100", numberOfDepartures:10000, timeRange: 43200) {aimedArrivalTime, serviceJourney{line{transportMode, id}}}
                evening:estimatedCalls(startTime: "2018-06-08T19:00:00+0100", numberOfDepartures:10000, timeRange: 14400) {aimedArrivalTime, serviceJourney{line{transportMode, id}}}
                night: estimatedCalls(startTime: "2018-06-08T23:00:00+0100", numberOfDepartures:10000, timeRange: 28800) {aimedArrivalTime, serviceJourney{line{transportMode, id}}}
        }
    }
    }"""

filename = "response.json"
file = open(filename, "w")
journeyplannerResponse = sendGraphqlQuery(query, {})
file.write(journeyplannerResponse)
file.close()

print("Everything went OK. Reponse has been written to " + filename)