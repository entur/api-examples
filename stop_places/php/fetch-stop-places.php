<?php

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

$query = <<<'JSON'
{
    topographicPlace(query: "Nesbru") {
        id
        name {
            value
        }
    }
}
JSON;
$variables = '';

$json = json_encode(['query' => $query, 'variables' => $variables]);
$hostname = gethostname();
$etClientName = "php-code-example-" . $hostname;
$request = curl_init();
curl_setopt($request, CURLOPT_URL, 'https://api.entur.org/stop_places/1.0/graphql/');
curl_setopt($request, CURLOPT_RETURNTRANSFER, true); 
curl_setopt($request, CURLOPT_CUSTOMREQUEST, 'POST');
curl_setopt($request, CURLOPT_HEADER, true);
curl_setopt($request, CURLOPT_VERBOSE, true);
curl_setopt($request, CURLOPT_POSTFIELDS, $json);
curl_setopt($request, CURLOPT_HTTPHEADER,
    array(
        'User-Agent: php code example',
        'Content-Type: application/json;charset=utf-8',
        "ET-Client-Name: $etClientName",
        "ET-Client-ID: $hostname"
    )
); 
$response = curl_exec($request);


print($response);


?>