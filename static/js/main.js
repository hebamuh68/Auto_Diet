(function () {
  "use strict";

    for(let i = 1; i < 4; i++)
    {
        const question = document.querySelector(`.question${i}`);

        question.addEventListener("click", function (event) {
          if ($(`.answer${i}`).css("display") === "none") {
            $(`.answer${i}`).css("display", "block");
          } else {
            $(`.answer${i}`).css("display", "none");
          }
        });
    }


})();
