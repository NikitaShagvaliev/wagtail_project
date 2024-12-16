function t396_scaleBlock(e){var t=t396_isOnlyScalableBrowser(),a=t396_detectResolution(e),l=document.getElementById("rec"+e);if(l){var o=l.querySelector(".t396__artboard"),r=t396_scale__getElementsToScale(o);if(o&&0!==r.length){var _;"function"==typeof window.t396__getCurrentScaleFactor?_=t396__getCurrentScaleFactor(e):(_=window.tn&&window.tn["ab"+e]&&window.tn["ab"+e].scaleFactor)||(_=window.tn_scale_factor);var i=t396_ab__getFieldValue(o,"height"),s=Math.floor(i*_),n;if(t396_ab__getFieldValue(o,"height_vh")){var c=t396_ab__getFieldValue(o,"height"),d=t396_ab__getHeight(o),u=c*_;s=u>=d?u:d}t396_scale__updateArtboardState(o,s),r.forEach((function(e){var l=e.querySelector(".tn-molecule, .tn-atom"),o=t396_scale__getElementType(e),r=t396_elem__getFieldValue(e,"container");if(r||"group"!==o||(r="grid"),l&&"grid"===r)if(t){var i=l.closest(".tn-atom__scale-wrapper");i||(t396_scale__wrapElement(l,_,"tn-atom__scale-wrapper"),i=l.closest(".tn-atom__scale-wrapper")),e.style.zoom="",t396_scale__processBackdropFilter(e,l,i),t396_scale__processBackgroundForShape(e,l,o,_)}else{var s=/^((?!chrome|android).)*safari/i.test(navigator.userAgent);if(("text"===o||"button"===o)&&s){e.style.zoom="";var n=parseFloat(getComputedStyle(l).fontSize),c=l.style.webkitTextSizeAdjust;l.style.webkitTextSizeAdjust="none",e.style.zoom=_;var d=Math.round(parseFloat(getComputedStyle(l).fontSize)),u=Math.abs(n-d);l.style.webkitTextSizeAdjust=c,u>=1&&(l.style.fontSize=Math.round(n*_)+"px",l.style.webkitTextSizeAdjust="none")}if("yes"!==e.getAttribute("data-scale-off")&&(e.style.zoom=_),"shape"===o){var p=t396_elem__getFieldValue(e,"height");p=t396_elem__getHeight(e,p),p=t396_elem__convertPosition__Local__toAbsolute(e,"height",p);var g=t396_elem__getFieldValue(e,"width");g=t396_elem__getWidth(e,g),g=t396_elem__convertPosition__Local__toAbsolute(e,"width",g);var m=parseFloat(t396_elem__getFieldValue(e,"top"));m=t396_elem__convertPosition__Local__toAbsolute(e,"top",m);var h=parseFloat(t396_elem__getFieldValue(e,"left"));h=t396_elem__convertPosition__Local__toAbsolute(e,"left",h);var f=window.getComputedStyle(l),y=f.borderWidth,b="none"!==f.backgroundImage,v=e.getAttribute("data-animate-sbs-event");if((p<=2||g<=2)&&"0px"===y&&!b&&!v){e.style.removeProperty("zoom");var w=g*_,F=p*_,S=m*_,A=h*_;e.style.width=parseFloat(w)+"px",e.style.height=parseFloat(F)+"px",e.style.top=Math.round(S)+"px",e.style.left=Math.round(A)+"px",e.setAttribute("data-scale-off","yes")}}"text"===o&&a<1200&&l&&!s&&(l.style.webkitTextSizeAdjust="auto"),l&&(l.style.transformOrigin="center")}}))}}}function t396_scale__getElementsToScale(e){return e?Array.prototype.slice.call(e.children).filter((function(e){return e&&(e.classList.contains("t396__elem")||e.classList.contains("t396__group"))})):[]}function t396_scale__updateArtboardState(e,t){e.classList.add("t396__artboard_scale");var a=e.getAttribute("data-artboard-recid"),l='<style class="t396__scale-style">.t-rec#rec'+a+" { overflow: visible; }#rec"+a+" .t396__carrier,#rec"+a+" .t396__filter,#rec"+a+" .t396__artboard {height: "+t+"px !important;width: 100vw !important;max-width: 100%;}</style>";e.insertAdjacentHTML("beforeend",l)}function t396_scale__wrapElement(e,t,a){if(e){var l=e.parentNode;if(l){var o=document.createElement("div");o.classList.add(a),o.style.transform="scale("+t+")",o.appendChild(e),l.appendChild(o)}}}function t396_scale__processBackdropFilter(e,t,a){"none"===e.style.backdropFilter&&(e.style.backdropFilter="");var l=getComputedStyle(e).backdropFilter;if(l){e.style.backdropFilter="none",a.style.backdropFilter=l;var o=getComputedStyle(t).borderRadius;"0px"!==o&&(a.style.borderRadius=o)}}function t396_scale__processBackgroundForShape(e,t,a,l){if("shape"===a){var o=t&&getComputedStyle(t),r;if(o)if((o&&o.backgroundImage||t.getAttribute("data-original"))&&"fixed"===o.backgroundAttachment){e.removeChild(t.parentNode),e.appendChild(t);var _=t396_elem__getFieldValue(e,"height");_=t396_elem__getHeight(e,_),_=t396_elem__convertPosition__Local__toAbsolute(e,"height",_);var i=t396_elem__getFieldValue(e,"width");i=t396_elem__getWidth(e,i),i=t396_elem__convertPosition__Local__toAbsolute(e,"width",i);var s=parseFloat(t396_elem__getFieldValue(e,"top")),n=parseFloat(t396_elem__getFieldValue(e,"left"));e.style.top=s*l+"px",e.style.left=n*l+"px",e.style.height=_*l+"px",e.style.width=i*l+"px",e.setAttribute("data-scale-off","yes")}}}function t396_scale__getElementType(e){var t=e.getAttribute("data-elem-type");return!t&&e.classList.contains("tn-group")&&(t="group"),t}window.t396_initialScale||(window.t396_initialScale=function(){});