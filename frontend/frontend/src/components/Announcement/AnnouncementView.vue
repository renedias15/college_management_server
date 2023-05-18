<template>
  <div class="announcement-board">
    <h2>Announcement Board</h2>
    <div v-for="announcement in announcements" :key="announcement[0]" class="announcement">
      <h3>{{ announcement[2]}}</h3>
      <p>{{ announcement[1] }}</p>
      <span class="date">{{ formatDate(announcement[3]) }}</span>
    </div>
    <div v-if="announcements.length === 0" class="no-announcements">
      No announcements for today.
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      announcements: [],
    };
  },
  mounted() {
    // Fetch announcements from the server
    this.fetchAnnouncements();
  },
  methods: {
    fetchAnnouncements() {
      axios.get('http://localhost:5000/getAnnouncements')
        .then(response => {
          this.announcements = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    formatDate(date) {
      return new Date(date).toLocaleDateString();
    },
  },
};
</script>

<style scoped>
.announcement-board {
  max-width: 600px;
  margin: 20px auto;
}

.announcement {
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
}

.announcement:hover {
  background-color: #f1f1f1;
}

.announcement-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.announcement-title {
  margin: 0;
  color: #333;
}

.announcement-date {
  color: #888;
  font-size: 0.9em;
}

.announcement-content {
  color: #666;
  line-height: 1.4;
}

.no-announcements {
  text-align: center;
  margin-top: 20px;
  color: #888;
  font-style: italic;
}
</style>







