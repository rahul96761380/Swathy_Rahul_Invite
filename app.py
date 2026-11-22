from pathlib import Path
import base64, json
import streamlit as st
import streamlit.components.v1 as components

ROOT=Path(__file__).resolve().parent
SLIDE_DIR=ROOT/"assets"/"slides"
MUSIC_FILE=ROOT/"assets"/"music"/"soft_carnatic_instrumental.mp3"
slides=[
 {"file":"01_krishna_blessings.jpg","kicker":"A BEAUTIFUL NEW CHAPTER","title":"A little\nmiracle","accent":"is on its way…","body":"A tiny new heartbeat,\na lifetime of love.","kind":"opening"},
 {"file":"02_krishna_radha.jpg","kicker":"LOVE, LAUGHTER & LITTLE MOMENTS","title":"A little mischief,","accent":"endless love…","body":"May our little one be surrounded\nby joy, wonder and love.","kind":"krishna"},
 {"file":"03_swathy_rahul.jpg","kicker":"OUR GREATEST ADVENTURE BEGINS","title":"Swathy &\nRahul","accent":"Our hearts are\ngrowing…","body":"Soon to be\nAmma & Appa","kind":"names"},
 {"file":"04_baby_shower.jpg","kicker":"A DAY FILLED WITH LOVE","title":"Join us for our","accent":"Baby Shower","body":"As we celebrate\nour little one on the way,\nwe would be delighted\nto have you with us.","kind":"invite"},
 {"file":"05_event_details.jpg","kicker":"SAVE THE DATE","title":"Friday, 12 February\n2027","accent":"6:30 AM","body":"Raghu Saran Mini Hall\nNo. 1, 1st Cross Street,\nLIC Colony, Pammal, Chennai\nTamil Nadu – 600075\n(Approx. 2 km from Pallavaram\nRailway Station)","kind":"details"},
 {"file":"06_closing_blessings.jpg","kicker":"A LITTLE LOVE MAKES A BIG BLESSING","title":"Your presence\nwill make our day","accent":"complete.","body":"With love and warm wishes,\nSwathy & Rahul","kind":"closing"}
]
st.set_page_config(page_title="Swathy & Rahul | Baby Shower",page_icon="🪷",layout="wide",initial_sidebar_state="collapsed")
missing=[s["file"] for s in slides if not (SLIDE_DIR/s["file"]).is_file()]
if missing:
 st.error("Missing slide artwork: "+", ".join(missing)+". Upload the complete assets/slides folder.")
 st.stop()
for s in slides:
 s["src"]="data:image/jpeg;base64,"+base64.b64encode((SLIDE_DIR/s["file"]).read_bytes()).decode("ascii")
slides_json=json.dumps(slides,ensure_ascii=False).replace("</","<\\/")
audio_data=("data:audio/mpeg;base64,"+base64.b64encode(MUSIC_FILE.read_bytes()).decode("ascii")) if MUSIC_FILE.is_file() else ""
html=r"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,viewport-fit=cover">
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Great+Vibes&family=Playfair+Display:wght@400;500;600;700&display=swap');
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:#160d0a}
#stage{position:relative;width:100%;height:calc(100vh - 68px);height:calc(100svh - 68px);height:calc(100dvh - 68px);min-height:0;overflow:hidden;color:#542d18;isolation:isolate;background:#160d0a}
#art{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;animation:zoom 8s ease-in-out both}
@keyframes zoom{from{transform:scale(1.02)}to{transform:scale(1.09)}}
#veil{position:absolute;inset:0;z-index:1;pointer-events:none;background:linear-gradient(180deg,rgba(25,12,5,.1),transparent 22%,transparent 75%,rgba(25,12,5,.2))}
#content{position:absolute;z-index:3;left:50%;top:36%;transform:translate(-50%,-50%);width:min(78%,740px);max-height:56%;overflow:hidden;padding:0 5px;text-align:center;background:transparent!important;border:0!important;border-radius:0!important;box-shadow:none!important;text-shadow:0 1px 2px rgba(255,247,226,.98),0 0 12px rgba(255,247,226,.9);display:flex;flex-direction:column;justify-content:center;align-items:center;gap:4px}
.kicker{font:600 clamp(11px,1.6vw,17px) 'Playfair Display',serif;letter-spacing:.2em;color:#9a6422;margin-bottom:12px}
.title{font:500 clamp(30px,5vw,68px)/1.1 'Playfair Display',serif;color:#67253a;margin:0}
.accent{font:500 clamp(34px,6vw,78px)/1.1 'Great Vibes',cursive;color:#7d263c;margin:8px 0}
.body{white-space:pre-line;font:500 clamp(18px,2.5vw,29px)/1.28 'Cormorant Garamond',serif;color:#56351f;margin-top:12px}
#content.opening{top:33%;width:76%;max-height:44%}
#content.krishna{top:72%;width:min(84%,720px);padding:12px 16px;border-radius:18px;background:transparent!important;border:0!important;box-shadow:none!important}
#content.krishna .kicker{margin:0 0 3px}#content.krishna .title{font-size:clamp(23px,3.7vw,46px)}#content.krishna .accent{font-size:clamp(26px,4vw,48px);margin:0}#content.krishna .body{font-size:clamp(15px,2vw,22px);margin-top:3px}
#content.names .title{font:500 clamp(43px,7vw,90px) 'Great Vibes',cursive}#content.names .accent{font:italic 500 clamp(23px,4vw,46px) 'Playfair Display',serif}#content.names .body{font:500 clamp(40px,7vw,82px) 'Great Vibes',cursive;color:#76253b}
#content.invite{top:43%}#content.invite .title,#content.invite .accent{font-size:clamp(38px,6vw,72px)}
#content.details{top:45%;width:min(78%,720px);max-height:68%;padding:16px 20px;background:transparent!important;border:0!important;box-shadow:none!important}
#content.details .kicker{margin:0 0 8px}#content.details .title{font-size:clamp(23px,3.8vw,46px)}#content.details .accent{font:600 clamp(27px,4.4vw,52px) 'Playfair Display',serif}#content.details .body{font-size:clamp(16px,2.15vw,24px);line-height:1.2;margin-top:6px}
#content.closing{top:44%;width:min(76%,740px)}#content.closing .title{font:italic 500 clamp(30px,5vw,60px) 'Playfair Display',serif}#content.closing .accent{font-size:clamp(32px,5.5vw,68px)}#content.closing .body{font:500 clamp(34px,5.5vw,62px) 'Great Vibes',cursive;color:#76253b}
#map{display:none;margin-top:12px;padding:10px 18px;border-radius:999px;background:#76253b;color:#fff8e9;text-decoration:none;font:600 15px 'Playfair Display',serif;text-shadow:none}
#content.details #map{display:inline-block}
#progress{position:absolute;z-index:8;top:0;left:0;width:100%;height:4px;background:#ffffff66}
#fill{height:100%;width:0;background:linear-gradient(90deg,#e6c06f,#fff0bc);box-shadow:0 0 12px #e5bd69}
#top{position:absolute;z-index:6;top:max(14px,env(safe-area-inset-top));left:18px;right:18px;display:flex;justify-content:space-between;color:#fff7e8;font:600 12px 'Playfair Display',serif;text-shadow:0 2px 8px #3b1d0c}
#controls{position:absolute;z-index:7;left:0;right:0;bottom:max(16px,env(safe-area-inset-bottom));display:flex;justify-content:center;align-items:center;gap:14px}
button{cursor:pointer}.ctrl{width:44px;height:44px;border:1px solid #fff2d6bb;border-radius:50%;background:#31180d88;color:#fff8e9;font-size:23px;backdrop-filter:blur(8px)}
.ctrl.main{width:52px;height:52px;background:#76253be8;border-color:#f3d99b;font-size:18px}
#dots{display:flex;gap:9px;align-items:center}.dot{width:8px;height:8px;padding:0;border:1px solid #fff;border-radius:50%;background:#fff8;}.dot.active{background:#f5d17c;transform:scale(1.4);box-shadow:0 0 10px #f5d17c}
#hint{position:absolute;z-index:6;bottom:78px;left:0;right:0;text-align:center;color:#fff5df;font:500 12px 'Playfair Display',serif;text-shadow:0 2px 6px #32170b}
@media(max-width:700px){
html,body{width:100%;height:100%;overflow:hidden;overscroll-behavior:none}
#stage{width:100vw;height:calc(100vh - 68px);height:calc(100svh - 68px);height:calc(100dvh - 68px);min-height:0}
#content{width:82%;max-width:520px;max-height:50%;padding:0 4px;border-radius:0;background:transparent!important;border:0!important;box-shadow:none!important;gap:2px;text-shadow:0 1px 2px rgba(255,247,226,.98),0 0 10px rgba(255,247,226,.9)}
.kicker{font-size:clamp(9px,2.5vw,12px);letter-spacing:.12em;margin-bottom:5px}
.title{font-size:clamp(25px,7vw,39px);line-height:1.08}
.accent{font-size:clamp(28px,8vw,43px);line-height:1.08;margin:4px 0}
.body{font-size:clamp(15px,4vw,19px);line-height:1.18;margin-top:5px}
#content.opening{width:82%;top:32%;max-height:40%}
#content.krishna{top:67%;width:82%;max-height:28%;padding:0;background:transparent!important}
#content.krishna .kicker{font-size:9px}#content.krishna .title{font-size:clamp(21px,6vw,31px)}#content.krishna .accent{font-size:clamp(25px,7vw,36px)}#content.krishna .body{font-size:clamp(13px,3.5vw,16px)}
#content.names{width:82%;top:36%;max-height:46%}#content.names .title{font-size:clamp(39px,11vw,58px)}#content.names .accent{font-size:clamp(20px,5.5vw,29px)}#content.names .body{font-size:clamp(30px,8vw,43px)}
#content.invite{width:82%;top:36%;max-height:46%}#content.invite .title,#content.invite .accent{font-size:clamp(30px,8vw,44px)}
#content.details{width:82%;top:36%;max-height:50%;padding:0;background:transparent!important}#content.details .title{font-size:clamp(20px,5.5vw,30px)}#content.details .accent{font-size:clamp(25px,7vw,38px)}#content.details .body{font-size:clamp(13px,3.5vw,17px);line-height:1.18}
#content.closing{width:82%;top:36%;max-height:46%;padding:0;background:transparent!important}#content.closing .title{font-size:clamp(25px,6.5vw,36px)}#content.closing .accent{font-size:clamp(29px,8vw,43px)}#content.closing .body{font-size:clamp(31px,8vw,44px)}
#controls{gap:8px;bottom:max(9px,env(safe-area-inset-bottom))}.ctrl{width:38px;height:38px}.ctrl.main{width:46px;height:46px}#dots{gap:7px}#hint{bottom:58px;font-size:10px}#top{top:max(9px,env(safe-area-inset-top));left:10px;right:10px;font-size:10px}
}
@media(orientation:landscape) and (max-height:560px){#content{top:48%;max-height:70%}#content.details{width:68%}#controls{bottom:7px}#hint{display:none}}

/* Balanced composition pass: keep each slide's copy in its own clear area */
#content{width:min(84%,760px);max-height:64%;gap:8px}
.kicker{font-size:clamp(12px,1.8vw,19px);letter-spacing:.16em;margin:0 0 8px}
.title{font-size:clamp(34px,5.5vw,72px);line-height:1.06}
.accent{font-size:clamp(38px,6vw,78px);line-height:1.04;margin:5px 0}
.body{font-size:clamp(20px,2.7vw,30px);line-height:1.25;margin-top:8px}
#content.opening{top:44%;width:78%;max-height:48%}
#content.opening .kicker{margin-bottom:6px}
#content.opening .title{font-size:clamp(34px,5.5vw,68px)}
#content.opening .accent{font-size:clamp(40px,6.5vw,76px)}
#content.krishna{top:22%;width:84%;max-height:32%;padding:8px 10px;gap:4px}
#content.krishna::before{content:"";position:absolute;inset:-14px -22px;z-index:-1;border-radius:50%;background:radial-gradient(ellipse,rgba(255,246,220,.76) 0%,rgba(255,246,220,.48) 55%,rgba(255,246,220,0) 100%)}
#content.krishna .kicker{font-size:clamp(10px,1.6vw,15px);margin:0 0 4px;color:#80501e}
#content.krishna .title{font-size:clamp(27px,4vw,45px);line-height:1.02}
#content.krishna .accent{font-size:clamp(31px,4.5vw,52px);margin:0}
#content.krishna .body{font-size:clamp(17px,2.3vw,24px);line-height:1.15;margin-top:3px}
#content.names{top:42%;width:84%;max-height:54%;gap:10px}
#content.names .title{font-size:clamp(48px,8vw,96px);line-height:1}
#content.names .accent{font-size:clamp(27px,4.3vw,49px);line-height:1.08}
#content.names .body{font-size:clamp(40px,7vw,78px);line-height:1}
#content.invite{top:43%;width:84%;max-height:55%;gap:9px}
#content.invite .title,#content.invite .accent{font-size:clamp(40px,6.3vw,76px)}
#content.invite .body{font-size:clamp(21px,3vw,32px)}
#content.details{top:49%;width:84%;max-height:64%;gap:9px}
#content.details .kicker{font-size:clamp(13px,1.8vw,19px);margin:0 0 4px}
#content.details .title{font-size:clamp(27px,4.4vw,52px);line-height:1.08}
#content.details .accent{font-size:clamp(38px,5.5vw,66px);margin:3px 0}
#content.details .body{font-size:clamp(18px,2.7vw,29px);line-height:1.22;margin-top:5px}
#content.details #map{margin-top:12px;padding:12px 22px;font-size:clamp(14px,1.8vw,18px)}
#content.closing{top:44%;width:82%;max-height:55%;gap:8px}
#content.closing .title{font-size:clamp(34px,5.3vw,64px)}
#content.closing .accent{font-size:clamp(39px,6vw,72px)}
#content.closing .body{font-size:clamp(40px,6vw,70px);line-height:1.02}

/* Phone layout: use the clear upper sky on the Krishna/Radha slide and center all other copy */
@media(max-width:700px){
  #content{width:88%;max-width:520px;max-height:58%;gap:5px;padding:4px 8px;
    text-shadow:0 1px 2px rgba(255,248,230,.98),0 0 8px rgba(255,248,230,.95),0 1px 5px rgba(255,248,230,.7)}
  .kicker{font-size:clamp(10px,2.8vw,13px);letter-spacing:.12em;margin:0 0 4px}
  .title{font-size:clamp(28px,7.5vw,40px);line-height:1.04}
  .accent{font-size:clamp(32px,8.5vw,46px);line-height:1.03;margin:3px 0}
  .body{font-size:clamp(17px,4.5vw,21px);line-height:1.16;margin-top:4px}
  #content.opening{top:43%;width:86%;max-height:40%}
  #content.opening .title{font-size:clamp(30px,8vw,42px)}
  #content.opening .accent{font-size:clamp(34px,9vw,47px)}
  #content.opening .body{font-size:clamp(17px,4.5vw,21px)}
  #content.krishna{top:20%;width:88%;max-height:30%;padding:6px 8px;gap:3px}
  #content.krishna::before{inset:-12px -16px;background:radial-gradient(ellipse,rgba(255,246,220,.88) 0%,rgba(255,246,220,.64) 58%,rgba(255,246,220,0) 100%)}
  #content.krishna .kicker{font-size:clamp(9px,2.5vw,12px);margin:0 0 2px}
  #content.krishna .title{font-size:clamp(24px,6.5vw,34px)}
  #content.krishna .accent{font-size:clamp(28px,7.5vw,39px)}
  #content.krishna .body{font-size:clamp(15px,4vw,18px);line-height:1.1;margin-top:2px}
  #content.names{top:41%;width:88%;max-height:52%;gap:7px}
  #content.names .title{font-size:clamp(43px,12vw,62px)}
  #content.names .accent{font-size:clamp(24px,6.5vw,34px)}
  #content.names .body{font-size:clamp(36px,10vw,52px)}
  #content.invite{top:42%;width:88%;max-height:52%;gap:7px}
  #content.invite .title,#content.invite .accent{font-size:clamp(34px,9vw,47px)}
  #content.invite .body{font-size:clamp(18px,4.8vw,23px)}
  #content.details{top:48%;width:88%;max-height:62%;gap:6px}
  #content.details .kicker{font-size:clamp(11px,3vw,14px);margin:0}
  #content.details .title{font-size:clamp(25px,6.8vw,36px)}
  #content.details .accent{font-size:clamp(34px,9vw,48px)}
  #content.details .body{font-size:clamp(16px,4.2vw,20px);line-height:1.14}
  #content.details #map{margin-top:7px;padding:10px 16px;font-size:14px}
  #content.closing{top:43%;width:88%;max-height:52%;gap:6px}
  #content.closing .title{font-size:clamp(28px,7.5vw,40px)}
  #content.closing .accent{font-size:clamp(34px,9vw,47px)}
  #content.closing .body{font-size:clamp(36px,9.5vw,51px)}
}


/* Final mobile spacing correction — especially slide 04 */
@media(max-width:700px){
  #content.invite{
    top:51% !important;
    width:90% !important;
    max-height:58% !important;
    gap:12px !important;
    padding:8px 10px !important;
  }
  #content.invite .kicker{
    font-size:clamp(11px,3.1vw,14px) !important;
    letter-spacing:.16em !important;
    margin:0 0 8px !important;
  }
  #content.invite .title{
    font-size:clamp(35px,9.2vw,49px) !important;
    line-height:1.08 !important;
  }
  #content.invite .accent{
    font-size:clamp(43px,11vw,58px) !important;
    line-height:1.02 !important;
    margin:2px 0 8px !important;
  }
  #content.invite .body{
    max-width:94%;
    font-size:clamp(19px,5vw,24px) !important;
    line-height:1.28 !important;
    margin-top:7px !important;
  }
}


/* Slide 01: keep every line inside the clear central parchment area marked by the user */
#content.opening{
  top:54% !important;
  left:50% !important;
  width:72% !important;
  max-height:34% !important;
  padding:4px 8px !important;
  gap:5px !important;
  overflow:visible !important;
}
#content.opening .kicker{
  font-size:clamp(10px,1.5vw,15px) !important;
  letter-spacing:.13em !important;
  line-height:1.15 !important;
  margin:0 0 3px !important;
}
#content.opening .title{
  font-size:clamp(29px,4.6vw,54px) !important;
  line-height:1.04 !important;
}
#content.opening .accent{
  font-size:clamp(35px,5.3vw,62px) !important;
  line-height:1.02 !important;
  margin:1px 0 3px !important;
}
#content.opening .body{
  font-size:clamp(17px,2.2vw,24px) !important;
  line-height:1.16 !important;
  margin-top:2px !important;
}
@media(max-width:700px){
  #content.opening{
    top:55% !important;
    width:72% !important;
    max-height:34% !important;
    padding:3px 5px !important;
    gap:4px !important;
  }
  #content.opening .kicker{
    font-size:clamp(9px,2.6vw,12px) !important;
    letter-spacing:.10em !important;
    margin:0 0 2px !important;
  }
  #content.opening .title{
    font-size:clamp(27px,7.5vw,36px) !important;
    line-height:1.03 !important;
  }
  #content.opening .accent{
    font-size:clamp(32px,8.5vw,42px) !important;
    line-height:1 !important;
    margin:0 !important;
  }
  #content.opening .body{
    font-size:clamp(16px,4.2vw,19px) !important;
    line-height:1.12 !important;
    margin-top:2px !important;
  }
}


/* FINAL TYPOGRAPHY + PILLAR SAFE-AREA PASS */
#content{left:50%;width:70%;max-width:650px;max-height:48%;overflow:hidden;gap:5px;padding:4px 2px;justify-content:center;text-align:center}
#content .kicker,#content .title,#content .accent,#content .body{white-space:pre-line;max-width:100%;overflow-wrap:break-word}
#content .kicker{font-size:clamp(11px,1.5vw,16px);line-height:1.15;letter-spacing:.13em;margin:0 0 3px}
#content .title{font-size:clamp(32px,4.5vw,54px);line-height:1.03;margin:0}
#content .accent{font-size:clamp(36px,5vw,62px);line-height:1.02;margin:1px 0}
#content .body{font-size:clamp(19px,2.4vw,27px);line-height:1.14;margin:3px 0 0}
#content.opening{top:54%;width:70%;max-height:37%;gap:4px}
#content.opening .title{font-size:clamp(31px,4.6vw,56px)}
#content.opening .accent{font-size:clamp(36px,5.1vw,62px)}
#content.krishna{top:24%;width:72%;max-height:34%;gap:4px}
#content.krishna .title{font-size:clamp(28px,4vw,46px)}
#content.krishna .accent{font-size:clamp(32px,4.5vw,52px)}
#content.krishna .body{font-size:clamp(18px,2.3vw,25px)}
#content.names{top:48%;width:70%;max-height:48%;gap:5px}
#content.names .title{font:500 clamp(42px,6.2vw,76px)/1.02 'Great Vibes',cursive}
#content.names .accent{font:italic 500 clamp(26px,3.7vw,43px)/1.08 'Playfair Display',serif}
#content.names .body{font:500 clamp(37px,5.5vw,66px)/1.02 'Great Vibes',cursive}
#content.invite{top:50%;width:70%;max-height:50%;gap:6px}
#content.invite .title{font-size:clamp(32px,4.6vw,55px)}
#content.invite .accent{font-size:clamp(40px,5.7vw,68px)}
#content.invite .body{font-size:clamp(20px,2.6vw,29px);line-height:1.16}
#content.details{top:49%;width:71%;max-height:58%;gap:5px;padding:2px}
#content.details .kicker{font-size:clamp(11px,1.5vw,16px);margin:0}
#content.details .title{font-size:clamp(27px,3.8vw,45px);line-height:1.05}
#content.details .accent{font:600 clamp(34px,4.8vw,57px)/1.02 'Playfair Display',serif}
#content.details .body{font-size:clamp(17px,2.25vw,25px);line-height:1.13;margin-top:2px}
#content.details #map{margin-top:6px;padding:9px 17px;font-size:clamp(13px,1.6vw,16px)}
#content.closing{top:49%;width:70%;max-height:50%;gap:5px}
#content.closing .title{font:italic 500 clamp(31px,4.5vw,54px)/1.04 'Playfair Display',serif}
#content.closing .accent{font-size:clamp(38px,5.3vw,64px)}
#content.closing .body{font:500 clamp(34px,5vw,60px)/1.04 'Great Vibes',cursive}
@media(max-width:700px){
 #content{width:69%;max-width:none;max-height:49%;gap:4px;padding:3px 1px}
 #content .kicker{font-size:clamp(9px,2.5vw,11px);letter-spacing:.10em;line-height:1.1;margin:0 0 2px}
 #content .title{font-size:clamp(25px,6.5vw,34px);line-height:1.02}
 #content .accent{font-size:clamp(29px,7.5vw,40px);line-height:1.01;margin:1px 0}
 #content .body{font-size:clamp(15px,3.9vw,19px);line-height:1.12;margin-top:2px}
 #content.opening{top:54%;width:69%;max-height:38%;gap:4px}
 #content.opening .title{font-size:clamp(26px,7vw,36px)}
 #content.opening .accent{font-size:clamp(31px,8vw,42px)}
 #content.opening .body{font-size:clamp(15px,4vw,19px)}
 #content.krishna{top:23%;width:70%;max-height:34%;gap:3px}
 #content.krishna .title{font-size:clamp(23px,6.1vw,31px)}
 #content.krishna .accent{font-size:clamp(27px,7vw,36px)}
 #content.krishna .body{font-size:clamp(14px,3.7vw,17px)}
 #content.names{top:48%;width:69%;max-height:50%;gap:5px}
 #content.names .title{font-size:clamp(36px,9.4vw,49px);line-height:1}
 #content.names .accent{font-size:clamp(22px,5.7vw,30px);line-height:1.04}
 #content.names .body{font-size:clamp(31px,8.2vw,43px);line-height:1}
 #content.invite{top:50%;width:69%;max-height:52%;gap:5px}
 #content.invite .title{font-size:clamp(27px,7.2vw,38px)}
 #content.invite .accent{font-size:clamp(34px,8.8vw,46px)}
 #content.invite .body{font-size:clamp(16px,4.2vw,20px);line-height:1.12}
 #content.details{top:48%;width:70%;max-height:60%;gap:4px;padding:1px}
 #content.details .kicker{font-size:clamp(9px,2.5vw,12px)}
 #content.details .title{font-size:clamp(23px,6vw,31px);line-height:1.02}
 #content.details .accent{font-size:clamp(29px,7.8vw,41px)}
 #content.details .body{font-size:clamp(13px,3.45vw,17px);line-height:1.1}
 #content.details #map{margin-top:4px;padding:8px 12px;font-size:12px}
 #content.closing{top:49%;width:69%;max-height:50%;gap:4px}
 #content.closing .title{font-size:clamp(25px,6.5vw,34px);line-height:1.02}
 #content.closing .accent{font-size:clamp(31px,8vw,42px)}
 #content.closing .body{font-size:clamp(29px,7.6vw,40px);line-height:1.02}
}

</style></head><body>
<div id="stage"><div id="progress"><div id="fill"></div></div>
<div id="top"><span>SWATHY &amp; RAHUL · BABY SHOWER</span><span id="counter">01 / 06</span></div>
<img id="art" alt="Royal illustrated invitation"><div id="veil"></div>
<div id="content"><div class="kicker" id="kicker"></div><h1 class="title" id="title"></h1><div class="accent" id="accent"></div><div class="body" id="body"></div>
<a id="map" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&amp;query=Raghu+Saran+Mini+Hall%2C+Pammal%2C+Chennai">⌖ &nbsp; Open in Google Maps</a></div>
<div id="hint">Tap to begin soft Carnatic music · Swipe to explore</div>
<div id="controls"><button class="ctrl" id="music" aria-label="Turn music off" title="Music on/off">♫</button><button class="ctrl" id="prev" aria-label="Previous">‹</button><div id="dots"></div><button class="ctrl main" id="play" aria-label="Pause">Ⅱ</button><button class="ctrl" id="next" aria-label="Next">›</button></div></div>
<script>
const slides=__DATA__,duration=8000,audioData=__AUDIO__;let idx=0,playing=true,elapsed=0,last=performance.now(),musicEnabled=true,musicStarted=false;
const art=document.getElementById('art'),content=document.getElementById('content'),fill=document.getElementById('fill'),dots=document.getElementById('dots'),play=document.getElementById('play'),musicBtn=document.getElementById('music');
const bgMusic=new Audio();bgMusic.loop=true;bgMusic.preload='auto';bgMusic.volume=0.30;if(audioData)bgMusic.src=audioData;else{musicEnabled=false;musicBtn.style.opacity='.45';musicBtn.title='Add the MP3 file described in README.md';}
const fields=['kicker','title','accent','body'];
function show(n){idx=(n+slides.length)%slides.length;let s=slides[idx];art.style.animation='none';void art.offsetWidth;art.src=s.src;art.style.animation='zoom 8s ease-in-out both';content.className=s.kind;fields.forEach(k=>document.getElementById(k).textContent=String(s[k]||'').replace(/\\n/g,'\n'));document.getElementById('counter').textContent=String(idx+1).padStart(2,'0')+' / 06';[...dots.children].forEach((d,i)=>d.classList.toggle('active',i===idx));elapsed=0;last=performance.now();fill.style.width='0%'}
slides.forEach((s,i)=>{let d=document.createElement('button');d.className='dot';d.setAttribute('aria-label','Slide '+(i+1));d.onclick=()=>show(i);dots.appendChild(d)});
document.getElementById('prev').onclick=()=>show(idx-1);document.getElementById('next').onclick=()=>show(idx+1);
function toggle(){playing=!playing;play.textContent=playing?'Ⅱ':'▶';play.setAttribute('aria-label',playing?'Pause':'Play');last=performance.now()}
play.onclick=toggle;
async function startMusic(){
 if(!audioData||!musicEnabled)return;
 try{await bgMusic.play();musicStarted=true;musicBtn.textContent='♫';musicBtn.style.opacity='1';document.getElementById('hint').textContent='Soft Carnatic music · Swipe to explore';}
 catch(e){document.getElementById('hint').textContent='Tap once to start the music · Swipe to explore';}
}
musicBtn.onclick=(e)=>{e.stopPropagation();if(!audioData){document.getElementById('hint').textContent='Add the MP3 file listed in README.md to enable music';return;}if(musicEnabled&&!musicStarted){startMusic();return;}musicEnabled=!musicEnabled;if(musicEnabled){startMusic();musicBtn.textContent='♫';}else{bgMusic.pause();musicBtn.textContent='♪';}};
document.getElementById('stage').addEventListener('pointerdown',()=>{if(musicEnabled&&!musicStarted)startMusic();});
if(audioData){startMusic();}
function loop(now){if(playing){elapsed+=now-last;fill.style.width=Math.min(100,elapsed/duration*100)+'%';if(elapsed>=duration)show(idx+1)}last=now;requestAnimationFrame(loop)}
document.addEventListener('keydown',e=>{if(e.key==='ArrowRight')show(idx+1);if(e.key==='ArrowLeft')show(idx-1);if(e.key===' '){e.preventDefault();toggle()}});
let sx=0,sy=0;document.getElementById('stage').addEventListener('touchstart',e=>{sx=e.changedTouches[0].screenX;sy=e.changedTouches[0].screenY},{passive:true});
document.getElementById('stage').addEventListener('touchend',e=>{let dx=e.changedTouches[0].screenX-sx,dy=e.changedTouches[0].screenY-sy;if(Math.abs(dx)>45&&Math.abs(dx)>Math.abs(dy))show(idx+(dx<0?1:-1))},{passive:true});
document.addEventListener('visibilitychange',()=>{if(document.hidden){playing=false;play.textContent='▶';bgMusic.pause()}else{playing=true;play.textContent='Ⅱ';last=performance.now();if(musicEnabled)startMusic()}});
show(0);requestAnimationFrame(loop);
</script></body></html>"""
html=html.replace("__DATA__",slides_json).replace("__AUDIO__",json.dumps(audio_data))
st.markdown("""
<style>
#MainMenu,
footer,
header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
.stAppDeployButton,
[data-testid="stAppDeployButton"] {
    display: none !important;
}
html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
section.main,
section.main > div,
[data-testid="stVerticalBlock"],
[data-testid="stElementContainer"] {
    height: 100% !important;
    max-height: 100% !important;
    overflow: hidden !important;
    margin: 0 !important;
    padding: 0 !important;
}
html, body, .stApp, [data-testid="stAppViewContainer"] {
    width: 100% !important;
    overscroll-behavior: none !important;
}
.block-container {
    width: 100% !important;
    max-width: 100% !important;
    height: 100dvh !important;
    max-height: 100dvh !important;
    padding: 0 !important;
    margin: 0 !important;
    overflow: hidden !important;
}
iframe[title="streamlit.components.v1.html"] {
    position: fixed !important;
    inset: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    height: 100svh !important;
    height: 100dvh !important;
    min-height: 0 !important;
    max-height: 100dvh !important;
    border: none !important;
    display: block !important;
    overflow: hidden !important;
    z-index: 999999 !important;
}
@media (max-width: 700px) {
    html, body, .stApp, [data-testid="stAppViewContainer"],
    [data-testid="stMain"], section.main, section.main > div,
    .block-container {
        height: 100dvh !important;
        min-height: 0 !important;
        max-height: 100dvh !important;
        overflow: hidden !important;
        position: fixed !important;
        inset: 0 !important;
    }
}
</style>
""", unsafe_allow_html=True)

components.html(html, height=900, scrolling=False)
