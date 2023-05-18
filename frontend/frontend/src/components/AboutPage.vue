<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-lg-6">
        <div class="card about-card">
          <img src="../.././images/cambridge.jpg" alt="University Image" class="card-img-top">
          <div class="card-body">
            <h2 class="card-title">About Our University</h2>
            <p class="card-text">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam quis eleifend magna, in mollis libero. Vivamus semper magna ut elementum scelerisque. Sed at placerat nisl, a vestibulum velit. Fusce convallis elit et metus facilisis, ac malesuada sapien fermentum. Integer nec leo quis neque faucibus rhoncus vel id dui. Nam condimentum augue nec erat cursus, in elementum nisl bibendum. Curabitur aliquet vestibulum lacus, nec fermentum enim tristique ut. Integer tincidunt tincidunt maximus.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.about-card {
  max-width: 100%;
  border: none;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin-bottom: 20px;
  margin-top: 20px;
  text-align: center;
}

.about-card .card-img-top {
  object-fit: cover;
  height: 300px;
}

.about-card .card-body {
  padding: 30px;
}

.about-card .card-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 15px;
}

.about-card .card-text {
  font-size: 16px;
  color: #333;
  line-height: 1.5;
}
</style>
