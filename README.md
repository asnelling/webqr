# webqr

Encode QR Codes as a (HTTP API) service

## Usage

1. Get the code

   ```Bash
   git clone https://github.com/asnelling/webqr
   cd webqr
   ```

2. Start a development server

   ```Bash
   flask --app webqr run
   ```

3. Generate a QR code

   ```Bash
   curl http://localhost:5000/qr/encode?data=foo
   ```
   
   The following query parameters are accepted:

   - `data`
   - `version`
   - `error_correction`
   - `box_size`
   - `border`

4. (Optional) Run the tests

   ```Bash
   python -m unittest
   ```
