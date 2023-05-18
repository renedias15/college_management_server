<template>
  <div>
    <div class="card" >
    <div class="card-header">
    <h2>Leave Requests</h2>
    </div>
      <div class="card-body">
    <div class="mb-3">
      <input type="text" class="form-control rounded-pill" placeholder="Search by name" v-model="searchText">
    </div>
    <table class="table table-striped table-bordered">
      <thead class="thead-dark">
        <tr>
          <th>Name</th>
          <th>Leave Type</th>
          <th>Reason</th>
          <th>From Date</th>
          <th>To Date</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="leaves in filteredLeaves" :key="leaves[1]">
           <td>{{ leaves[0] }}</td>
          <td>{{ leaves[3] }}</td>
          <td>{{ leaves[4] }}</td>
          <td>{{ leaves[5] }}</td>
          <td>{{ leaves[6] }}</td>
          <td>
            <button class="btn btn-success mr-2" @click="ApproveLeave(leaves[1])">Approve</button>
            <button class="btn btn-danger" @click="RejectLeave(leaves[1])">Reject</button>
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
Vue.use(VueAxios, axios)

export default {
  data() {
    return {
      leaves: [],
      searchText: ''
    };
  },
  mounted() {
    this.fetchLeaveRequests();
  },
  computed: {
    filteredLeaves() {
      // Filter the students based on the search text
      return this.leaves.filter(leaves => {
        const name = leaves[0].toLowerCase();
        const search = this.searchText.toLowerCase();
        return name.includes(search);
      });
    }
  },
  methods: {
    fetchLeaveRequests() {
      axios.get('http://localhost:5000/getLeaveRequests')
        .then(response => {
          this.leaves = response.data;
        })
        .catch(error => {
          console.error('Error fetching students:', error);
        });
    },
    ApproveLeave(leaveId) {
       const confirmation = window.confirm('Are you sure you want to approve this leave?');
        if (!confirmation) {
            return; // Cancel the update if the user cancels the confirmation
        } 
      axios.delete(`http://localhost:5000/approveLeave/${leaveId}`)
        .then(response => {
          console.warn(response)
          this.leaves = this.leaves.filter(leaves => leaves[1] !== leaveId);
        })
        .catch(error => {
          console.error('Error deleting student:', error);
        });
    },
     RejectLeave(leaveId) {
        const reason = window.prompt('Please provide a reason for rejecting this leave:');
        if (reason === null) {
            return; // Cancel the update if the user cancels the prompt
        }
       const confirmation = window.confirm('Are you sure you want to reject this leave?');
        if (!confirmation) {
            return; // Cancel the update if the user cancels the confirmation
        } 
      axios.delete(`http://localhost:5000/rejectLeave/${leaveId}`,{ data: { reason: reason } })
        .then(response => {
          console.warn(response)
          this.leaves = this.leaves.filter(leaves => leaves[1] !== leaveId);
        })
        .catch(error => {
          console.error('Error deleting student:', error);
        });
    },

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