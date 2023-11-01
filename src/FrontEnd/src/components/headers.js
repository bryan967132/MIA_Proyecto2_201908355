export const headers = new Headers()
export const API = 'http://3.139.93.27:5000';
headers.append('Content-Type', 'application/json');
headers.append('Accept', 'application/json');
headers.append('Access-Control-Allow-Origin', API);
headers.append('Access-Control-Allow-Credentials', 'true');
headers.append('GET', 'POST', 'OPTIONS', 'PUT', 'DELETE')