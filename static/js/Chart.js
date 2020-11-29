var team_names = []
var team_questions = []
for (let i = 0; i < teams_and_questions.length; i++) {
    team_names.push(teams_and_questions[i].split(';')[1].split('&')[0].split('?')[0]);
    team_questions.push(parseInt(teams_and_questions[i].split(';')[1].split('&')[0].split('?')[1]))
}
var ranks = []
for (let i=0;i<team_ranks.length;i++){
    ranks.push(team_ranks[i].split(';')[1].split('&')[0]);
}

var rankTable = document.getElementById("rank-table-menu")

rankTable.innerHTML=`<div class="rank-box" style="display:flex;align-items:center">
<div class="rank-team-name"style="color:white">Team Name</div>
<div class="rank-cur-que" style="padding-right:30px; text-align:right">Rank</div>
</div>`;
for (let i = 0; i < team_ranks.length; i++) {
    rankTable.innerHTML += `<div class="rank-box" style="display:flex;align-items:center">
                            <div class="rank-team-name" >${ranks[i]}</div>
                            <div class="rank-cur-que" >${i+1}</div>
                        </div>`
}       

var config = {
    type: 'line',
    data: {
        labels: team_names,//['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', 'sdklf', 'sdfsd', 'sdfsdf', 'sdfs', 'sdfsdf', 'sdfsdfds', 'sdfdsfds'],
        datasets: [{
            label: 'Question',
            data: team_questions,//[12, 19, 3, 5, 2, 3, 2, 3, 4, 5, 6, 7, 8],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            fill: false,
            pointRadius: 10,
            pointHoverRadius: 15,
            showLine: false
        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: '',
            fontColor: 'white'
        },
        legend: {
            display: false
        },
        elements: {
            point: {
                pointStyle: 'triangle'
            }
        },
        scales: {
            xAxes: [{
                display: true,
                gridLines: {
                    display: false,
                },
                ticks: {
                    fontColor: '#bfd9e7'
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Teams',
                    fontColor: '#bfd9e7',
                    fontSize: 15
                }
            }],
            yAxes: [{
                // display:false,
                ticks: {
                    beginAtZero: true,
                    max: 13,
                    min: 0,
                    stepSize: 1,
                    fontColor: '#4d6f83',
                    fontSize: 15
                },
                gridLines: {
                    // display:false
                    color: '#1e2d35'
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Current Question',
                    fontColor: '#bfd9e7'
                }
            }],
        },
    },
    animation: {
        animateScale: true
    }
};
var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, config);
function ranking() {
    document.getElementsByClassName('questions')[0].style.display = "none";
    document.getElementsByClassName('team')[0].style.display = "none";
    document.getElementsByClassName('ranking')[0].style.display = "block";
    document.getElementsByClassName('profile')[0].style.display = "none";
    document.getElementsByClassName('result')[0].style.display = "none";
    document.getElementsByClassName('contact')[0].style.display = "none";
    var question_menu = document.getElementById('questions-menu');
    var team_menu = document.getElementById('team-menu');
    var ranking_menu = document.getElementById('ranking-menu');
    var profile_menu = document.getElementById('profile-menu');
    var result_menu = document.getElementById('result-menu');
    var contact_menu = document.getElementById('contact-menu');
    var menu_text = document.getElementById('menu-selected-text');
    question_menu.className = 'menu-not-selected'
    team_menu.className = 'menu-not-selected'
    ranking_menu.className = 'menu-selected'
    profile_menu.className = 'menu-not-selected'
    result_menu.className = 'menu-not-selected'
    contact_menu.className = 'menu-not-selected'
    menu_text.innerText = 'Ranking'
    chart.destroy();
    chart = new Chart(ctx, config);
}