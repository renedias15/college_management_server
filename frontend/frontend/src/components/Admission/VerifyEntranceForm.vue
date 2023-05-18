<template>
  <div>
    <div class="card" >
        <div class="help-icon">
    <i class="fas fa-question-circle" @mouseover="showHelp = true" @mouseleave="showHelp = false" ></i>
    <div class="help-text" v-if="showHelp">
      <p>Every course has a pre-requisite,verify the documents->check for grades,subjects</p>
    </div>
  </div>
    <div class="card-header">
    <h2>Applicant List</h2>
    </div>
      <div class="card-body">
    <div class="mb-3">
      <input type="text" class="form-control rounded-pill" placeholder="Search by email" v-model="searchText">
    </div>
    <table class="table table-striped table-bordered">
      <thead class="thead-dark">
        <tr>
          <th>Email</th>
          <th>Name</th>
          <th>Course</th>
          <th>Photo</th>
          <th>Marksheet</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="ent_form in filteredForms" :key="ent_form[0]">
          <td>{{ ent_form[1] }}</td>
          <td>{{ ent_form[2] }}</td>
          <td>{{ ent_form[3] }}</td>
          <td> <a :href="'http://localhost:5000/'+ent_form[4]" target="_blank">Image</a></td>
          <td> <a :href="'http://localhost:5000/'+ent_form[5]" target="_blank">Image</a></td>
          <td>
            <button class="btn btn-success mr-2" @click="Elligible(ent_form[0],'A')">Elligible</button>
            <button class="btn btn-danger" @click="NonElligible(ent_form[0],'R')">Non Elligible</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  </div>
  
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
Vue.use(VueAxios,axios)

export default {
  data() {
    return {
      ent_forms: [],
       searchText: '',
       showHelp: false
    };
  },
  mounted() {
    this.fetchForms();
  },
  computed: {
    filteredForms() {
      // Filter the students based on the search text
      return this.ent_forms.filter(ent_form => {
        const name = ent_form[1].toLowerCase();
        const search = this.searchText.toLowerCase();
        return name.includes(search);
      });
    }
  },
  methods: {
    fetchForms() {
      axios.get('http://localhost:5000/getEnteranceForms')
        .then(response => {
          this.ent_forms = response.data;
        })
        .catch(error => {
          console.error('Error fetching forms:', error);
        });
    },
    Elligible(id,res){
        const confirmation = window.confirm('are you sure?');
        if (!confirmation) {
            return; // Cancel the update if the user cancels the confirmation
        }
        axios.put(`http://localhost:5000/verifyApplicant/${id}/${res}`)
        .then(response => {
          console.warn(response)
          this.ent_forms = this.ent_forms.filter(ent_forms => ent_forms[0] !== id);
        })
        .catch(error => {
          console.error('Error :', error);
        });
    },
    NonElligible(id,res){
        const confirmation = window.confirm('are you sure??');
        if (!confirmation) {
            return; // Cancel the update if the user cancels the confirmation
        }
        axios.put(`http://localhost:5000/verifyApplicant/${id}/${res}`)
        .then(response => {
          console.warn(response)
          this.ent_forms = this.ent_forms.filter(ent_forms => ent_forms[0] !== id);
        })
        .catch(error => {
          console.error('Error :', error);
        });
    }
  }
};
</script>
<style scoped>
.card{
    max-width: 100%;
    margin: 20px;
  border-radius: 15px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
}
.help-icon {
  position: absolute;
  top: 10px;
  left: 10px;
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