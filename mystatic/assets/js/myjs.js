$(document).ready(
    function (){
        const btn1 = $("#btn1");
        btn1.click(
            () => {
                    setInterval(does, 1000);
            }
        )
    }
)
counter = 0
function does(){
        btn1.text = counter.toString()
        counter+=1
}

