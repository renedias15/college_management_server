<template>
    <div class="container">
        <div class="help-icon mr-2">
              <i class="fas fa-question-circle" @mouseover="showHelp = true" @mouseleave="showHelp = false"></i>
              <div class="help-text" v-if="showHelp">
                <p>After printing , must get it stamped by principal </p>
              </div>
            </div>
      <div class="row">
        <div class="col-md-6">
        
          <div class="certificate" ref="certificate">
            <div class="text-center mb-4">
              <img src="../../.././images/logo.png" width="100px" height="100px" alt="Company Logo" class="logo">
              <h2 class="mb-0">Bonafide Certificate</h2>
            </div>
            
            <div class="text-center mb-4">
              <p>This is to certify that <strong>{{ studentName }}</strong> is a bonafide student of <strong>{{ institution }}</strong>.</p>
              <p>This certificate is issued for the purpose of <strong>{{ purpose }}</strong>.</p>
            </div>
            <div class="text-center">
              <p>Date: <strong>{{ date }}</strong></p>
              <p>Authorized Signatory</p><br><br>
            </div>
          </div>
        </div>

        <div class="col-md-6">
          <!-- Form content -->
          <div class="text-center">
            <div class="card">
              <div class="card-header">
                <h2>Enter details</h2>
              </div>
              <div class="card-body">
                <div class="form-group">
                  <input type="text" id="studentName" v-model="studentName" placeholder="Enter full name" class="form-control">
                </div>
                <div class="form-group">
                  <input type="text" id="institution" v-model="institution" placeholder="Enter institution name" class="form-control">
                </div>
                <div class="form-group">
                  <input type="text" id="purpose" v-model="purpose" placeholder="Enter purpose" class="form-control">
                </div>
                <button type="submit" class="btn btn-primary" @click="generateImage">Generate</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import html2canvas from 'html2canvas';

export default {
  name: 'BonafideCertificate',
  data() {
    return {
      studentName: '',
      institution: '',
      purpose: '',
      date: new Date().toLocaleDateString(),
      showHelp: false
    };
  },
  methods: {
    generateImage() {
      const certificateElement = this.$refs.certificate;

      // Use html2canvas to capture the certificate content as an image
      html2canvas(certificateElement).then(canvas => {
        // Convert the canvas to an image data URL
        const imageDataURL = canvas.toDataURL('image/png');

        // Create a link element to download the image
        const link = document.createElement('a');
        link.href = imageDataURL;
        link.download = 'bonafide_certificate.png';
        link.click();
      });
    }
  }
};
</script>

<style scoped>
.certificate {
  max-width: 600px;
  margin-top: 20px;
  background-color: #f9f9f9;
  padding: 20px;
  border: 1px solid #ccc;
}
.logo {
  max-width: 150px;
  margin-bottom: 20px;
}
.card {
  max-width: 800px;
  margin: 20px;
  border-radius: 15px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
}
.card-header {
  background-color: #3f51b5;
  color: #fff;
  border-radius: 15px 15px 0 0;
  padding: 10px 20px;
}

.card-body {
  padding: 20px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  font-weight: bold;
}

.btn-primary {
  background-color: #3f51b5;
  border-color: #3f51b5;
  margin-top: 20px;
}
#signature{
    border: solid 1px;
    border-color: #000;
}
.help-icon {
   position: relative;
  top: 100%;
  float: left;
  z-index: 1;
}

.help-text {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  width: 200px;
  padding: 10px;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.help-icon:hover .help-text {
  display: block;
}
</style>