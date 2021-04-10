const $forms = document.querySelectorAll(".signup-form");

const getTemplate = () => {
  return fetch("./template.html").then((response) => response.text());
};

const sendEmailToApi = (address, template) => {
  fetch(`https://bedu-email-sender-api.herokuapp.com/send`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      address: address,
      template: template,
    }),
  })
    .then((results) => {
      console.log(results);
    })
    .catch((error) => {
      console.error(error);
    });
};

const sendEmail = (event) => {
  event.preventDefault();
  const email = event.target.querySelector("input").value;
  getTemplate()
    .then((template) => {
      sendEmailToApi(email, template);
    })
    .catch((error) => {
      console.log(error, "error al convertir el template.");
    });
};

for (let i = 0; i < $forms.length; i++) {
  $forms[i].addEventListener("submit", sendEmail);
}

/***************Mi codigo*****************************/

const mainText = document.getElementById("mainText");
mainText.addEventListener("click", function () {
  if(this.style.color !== "#b9264b")
      this.style.color = "#D8abb1";
  else
      this.style.color ="#b9264b";

})

var Data = function (nameProduct, tradeMark, imgSrc) {
    this.nameProduct = nameProduct;
    this.tradeMark = tradeMark;
    this.imgSrc = imgSrc;
}

function createElements(tag,text) {
  const element = document.createElement(tag);
  if(typeof text !== "undefined") {
    element.innerText = text;
  }
  return element;
}

function createSection (productOne) {
    var article = document.createElement("article");
    var firstSection = document.createElement("div");
    var secondSection = document.createElement("img");
    var threeSection = document.createElement("div");

    var h3 = createElements("h3",productOne.nameProduct);
    var h4 = createElements("h4",productOne.tradeMark);

    var link1 = document.createElement("a");
    var strong = document.createElement("strong");

    article.className = "item-compare";
    firstSection.className = "header-footer";

    secondSection.src = productOne.imgSrc;
    secondSection.alt = productOne.imgAlt;
    threeSection.className = "header-footer";

    link1.href = compare;

    strong.innerText = "Compara $";
    link1.appendChild(strong);

    firstSection.appendChild(h3);
    firstSection.appendChild(h4);

    threeSection.appendChild(link1);
    threeSection.appendChild(colorHeart());

    article.appendChild(firstSection);
    article.appendChild(secondSection);
    article.appendChild(threeSection);

    return article;
}
function createProduct() {
  const section = document.getElementById("compareArticle");
  var productOne = new Data(nameProduct, mark, imagen1);
  for(var i=0; i<12; i++)
  {
    section.appendChild(createSection(productOne));
  }

}

createProduct()

/*Modificando el color del corazon */
function colorHeart(){
  var heart = document.createElement("a");
  heart.href = heartLink;
  const offState = "heart-shape";
  const onState = `${offState} otherclass`;
  heart.className = offState;
  heart.addEventListener("click", function() {
    if(this.className === offState) {
      this.className = onState;
    }
    else {
      this.className = offState;
    }
  });

  return heart;
}


function changeButton(){
  var buttonOne = document.getElementById("button_one").onclick();
  var buttonTwo = document.getElementById("Button_two").onclick();

  if(buttonOne){
    buttonOne.style.visibility = 'hiden';
    buttonTwo.style.visibility = 'visible';
  }
  else{
    buttonOne.style.visibility = 'vosible';
    buttonTwo.style.visibility = 'hiden'; 
  }

}

