<template>
  <div class="container">
    <div class="card">
      <div class="card-body">
        <h2>Daily Announcement</h2>
        <div class="form-group">
          <label for="announcement">Write an announcement:</label>
          <input type="text" id="announcement" v-model="title" class="form-control" placeholder="Enter suitable title"> 
        </div>
        <div class="form-group"> 
          <textarea type="text" id="announcement" v-model="announcement" class="form-control" placeholder="Enter details here    "></textarea>
        </div>
        <button class="btn btn-primary" @click="postData">Post</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      announcement: '',
      title:''
    };
  },
   methods:{
    postData(e)
    {
      axios.post('http://localhost:5000/addAnnouncement', { announcement: this.announcement,title:this.title })
      .then((res)=>{
        console.warn(res);
      })
      e.preventDefault()
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin-top: 20px;
}
.card{
  max-width: 100%;
  margin: 20px;
  border-radius: 15px;
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.3);
}
.form-group {
  margin-bottom: 20px;
}

.btn-primary {
  background-color: #3f51b5;
  border-color: #3f51b5;
}
</style>