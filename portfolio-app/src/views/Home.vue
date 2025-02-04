<template>
  <div class="main-page container shadow p-5 mh-100vh">
    <header>
      <h1>Masterskaya — ваш надежный помощник в мире услуг!</h1>
    </header>

    <div class="container">
      <p>Добро пожаловать в Masterskaya — уникальное веб-приложение, созданное для тех, кто предлагает свои навыки и
        таланты в самых разных сферах. От фриланса и творческого рукоделия до профессиональных услуг — здесь вы найдете
        все необходимое для эффективного управления своим делом.</p>

      <p>С Masterskaya вы сможете:</p>
      <ul>
        <li>✅ <strong>Хранить информацию</strong> о своих услугах в одном удобном месте.</li>
        <li>✅ <strong>Обновлять данные</strong> быстро и без лишних усилий.</li>
        <li>✅ <strong>Распространять информацию</strong> среди клиентов, чтобы вас могли легко найти.</li>
      </ul>

      <p>Неважно, вы — опытный мастер или только начинаете свой путь, Masterskaya поможет вам организовать свою
        деятельность, привлечь новых заказчиков и сосредоточиться на том, что у вас получается лучше всего.</p>

      <a href="#" class="cta-button">Начните прямо сейчас!</a>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>

header {
  background-color: #e0c652;
  color: white;
  padding: 20px 0;
  text-align: center;
}

.container {
  max-width: 900px;
  margin: 20px auto;
  padding: 20px;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
  margin-top: 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

ul li {
  background: #f4f4f4;
  margin: 10px 0;
  padding: 10px;
  border-left: 5px solid #e0c652;
}

.cta-button {
  display: inline-block;
  background-color: #e0c652;
  color: white;
  padding: 10px 20px;
  text-decoration: none;
  font-size: 18px;
  margin-top: 20px;
  border-radius: 5px;
}

.cta-button:hover {
  background-color: #45a049;
}

</style>