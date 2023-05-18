<template>
  <div >
    <div class="card" >
    <div class="card-header">
    <h2>Student List</h2>
    </div>
      <div class="card-body">
    <div class="mb-3">
      <input type="text" class="form-control rounded-pill" placeholder="Search by name" v-model="searchText">
    </div>
    <table class="table table-striped table-bordered">
      <thead class="thead-dark">
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Surname</th>
          <th>Age</th>
          <th>Address</th>
          <th>Phone</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="student in filteredStudents" :key="student[0]">
           <td>{{ student[0] }}</td>
          <td>{{ student[1] }}</td>
          <td>{{ student[2] }}</td>
          <td>{{ student[3] }}</td>
          <td>{{ student[4] }}</td>
          <td>{{ student[5] }}</td>
          <td>
            <router-link :to="{ name: 'EditStudent', params: { id: student[0] } }" class="btn btn-primary">Edit</router-link>
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
      students: [],
       searchText: ''
    };
  },
  mounted() {
    this.fetchStudents();
  },
  computed: {
    filteredStudents() {
      // Filter the students based on the search text
      return this.students.filter(student => {
        const name = student[1].toLowerCase();
        const search = this.searchText.toLowerCase();
        return name.includes(search);
      });
    }
  },
  methods: {
    fetchStudents() {
      axios.get('http://localhost:5000/getStudents')
        .then(response => {
          this.students = response.data;
        })
        .catch(error => {
          console.error('Error fetching students:', error);
        });
    }
  }
};
</script>
<style scoped>
.card {
  max-width: 100%;
  margin: 20px;
  border-radius: 15px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
}
</style>