
<!doctype html>
<html>
  <head>
    
      <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <title>Smart Solar Optimizer User Guide (for web publish)</title>
    <link rel="shortcut icon" href="/favicon.ico">
    <style type="text/css">
      body {
        background-color: #EEEEEE;
        margin: 0;
        font-family: arial, sans, sans-serif;
      }
      #iframe-wrapper {
        height: 85vh;
        margin: auto;
        width: 100%;
        background: white;
        box-shadow: 0 0 0 0.75pt #d1d1d1,0 0 3pt 0.75pt #ccc;
        transition: height 0.5s ease, width 0.5s ease;
        position: relative;
        max-width: 834px;
      }

      #iframe-wrapper.loading:before {
        content: 'Loading...';
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background: white;
        text-align: center;
        line-height: 300px;
        font-family: 'Helvetica';
      }

      iframe {
        margin: auto;
        max-width: 794px;
        width: 100%;
        height: 100%;
        border: none;
        display: block;
      }
      footer p {
        text-align: center;
        padding: 15px;
        margin: 0;
        font-size: 12px;
        font-family: 'Helvetica';
        max-width: 700px;
        margin: auto;
        line-height: 1.4em;
      }

      footer p.warning {
        font-size: 0.7em;
      }

      #original {
        position: fixed;
        bottom: 0;
        right: 10px;
        text-align: center;
        background-color: white;
        padding: 5px 10px;
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        font-size: 0.7em;
        box-shadow: 0 0 10px #ddd;
        font-family: 'Helvetica';
      }

      #original:hover {
        opacity: 1;
      }

      body.markdown #iframe-wrapper {
        padding: 40px;
        box-sizing: border-box;
      }

      body.markdown #iframe-wrapper h1 {
        text-align: center;
      }

      @media only screen and (max-width: 800px) {
        #iframe-wrapper {
          max-width: none;
        }
        #original {
          position: relative;
          border-radius: 0;
          right: 0;
          margin-top: 1rem;
        }
      }

      @media print {
        body {
          background: none;
        }
        p {
          display: none;
        }
        #iframe-wrapper {
          height: auto;
          max-width: none;
          box-shadow: none;
          padding-top: 0;
          width: 100%;
        }
        iframe {
          max-width: none;
          width: 100%;
        }
        #original {
          display: none;
        }
      }

    </style>
  </head>
  <body class="">
    <div id="iframe-wrapper">
      <iframe id="googledoc" src="/raw/doc/e/2PACX-1vTs0NX90_rnbBuSM_0nAhNMnn8y7BUNteWhV10gXyFhr6kfGvg0K86TIsvYs7_rFE5jIaLMeKfQycw9"></iframe>
    </div>
    <div id="original">Document doesn't display correctly?<br /><a href="https://docs.google.com/document/d/e/2PACX-1vTs0NX90_rnbBuSM_0nAhNMnn8y7BUNteWhV10gXyFhr6kfGvg0K86TIsvYs7_rFE5jIaLMeKfQycw9/pub">See the original Google Doc</a></div>
    <footer>
      <p>Published with <a href="https://gdoc.pub" target="_blank">The Google Doc Publisher</a></p>
      <p class="warning">
        Be aware that <a href="https://gdoc.pub" target="_blank">gdoc.pub</a> is <strong>not</strong> responsible for the document's content.<br/>
        Something malicious? <a href="https://augustin-riedinger.fr/contact/" target="_blank">Write me</a>. You can also <a href="https://docs.google.com/abuse?id=e/2PACX-1vTs0NX90_rnbBuSM_0nAhNMnn8y7BUNteWhV10gXyFhr6kfGvg0K86TIsvYs7_rFE5jIaLMeKfQycw9" target="_blank">report abuse to Google</a>.
      </p>
    </footer>
    <script type="text/javascript">
      (function(){
        // From https://pawelgrzybek.com/page-scroll-in-vanilla-javascript/
        function scrollIt(a){var c=1<arguments.length&&arguments[1]!==void 0?arguments[1]:200,d=2<arguments.length&&arguments[2]!==void 0?arguments[2]:'linear',e=arguments[3],f={linear:function linear(m){return m},easeInQuad:function easeInQuad(m){return m*m},easeOutQuad:function easeOutQuad(m){return m*(2-m)},easeInOutQuad:function easeInOutQuad(m){return 0.5>m?2*m*m:-1+(4-2*m)*m},easeInCubic:function easeInCubic(m){return m*m*m},easeOutCubic:function easeOutCubic(m){return--m*m*m+1},easeInOutCubic:function easeInOutCubic(m){return 0.5>m?4*m*m*m:(m-1)*(2*m-2)*(2*m-2)+1},easeInQuart:function easeInQuart(m){return m*m*m*m},easeOutQuart:function easeOutQuart(m){return 1- --m*m*m*m},easeInOutQuart:function easeInOutQuart(m){return 0.5>m?8*m*m*m*m:1-8*--m*m*m*m},easeInQuint:function easeInQuint(m){return m*m*m*m*m},easeOutQuint:function easeOutQuint(m){return 1+--m*m*m*m*m},easeInOutQuint:function easeInOutQuint(m){return 0.5>m?16*m*m*m*m*m:1+16*--m*m*m*m*m}},g=window.pageYOffset,h='now'in window.performance?performance.now():new Date().getTime(),i=Math.max(document.body.scrollHeight,document.body.offsetHeight,document.documentElement.clientHeight,document.documentElement.scrollHeight,document.documentElement.offsetHeight),j=window.innerHeight||document.documentElement.clientHeight||document.getElementsByTagName('body')[0].clientHeight,k='number'==typeof a?a:a.offsetTop,l=Math.round(i-k<j?i-j:k);function b(){var m='now'in window.performance?performance.now():new Date().getTime(),n=Math.min(1,(m-h)/c),o=f[d](n);return window.scroll(0,Math.ceil(o*(l-g)+g)),window.pageYOffset===l?void(e&&e()):void requestAnimationFrame(b)}return!1=='requestAnimationFrame'in window?(window.scroll(0,l),void(e&&e())):void b()}

        var $iframe = document.getElementById('googledoc');
        if (!$iframe) return;
        var $iframeWrapper = document.getElementById('iframe-wrapper');
        var isSheet = document.location.pathname.indexOf('/sheet') === 0;

        if (isSheet) {
          $iframeWrapper.className = 'loading';
        }

        $iframe.addEventListener('load', function(e){
          var $table;
          if (isSheet) {
            $table = $iframe.contentWindow.document.getElementsByTagName('table')[0];
            $iframeWrapper.style.width = $table.offsetWidth+'px';
          }
          setTimeout(function(){
            var height, width;
            if (isSheet) {
              var $topBar = $iframe.contentWindow.document.getElementById('top-bar');
              height = $table.offsetHeight + $topBar.offsetHeight;
            } else {
              height = $iframe.contentWindow.document.body.offsetHeight+50;
            }
            $iframeWrapper.style.height = height+'px';
            setTimeout(function(){
              $iframeWrapper.className = '';
              if (!isSheet && window.location.hash && window.location.hash[0] === '#') {
                scrollIt($iframe.contentWindow.document.getElementById(window.location.hash.replace(/^#/, '')), 250, 'easeInOutQuad');
              }
            }, 500);
          }, 500);
        });

      })();

      (function(){
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

        ga('create', 'UA-36223212-9', 'auto');
        ga('send', 'pageview');
      })();
    </script>
  </body>
</html>
