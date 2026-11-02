// HTML image-map coordinates are defined in the SVG's intrinsic 700 × 760 space.
// Keep the clickable regions aligned with the illustration as it scales.
const mapImage = document.getElementById('germany-map');
if (mapImage) {
  const areas = document.querySelectorAll('map[name="germany"] area');
  const resizeAreas = () => {
    const scaleX = mapImage.clientWidth / 700;
    const scaleY = mapImage.clientHeight / 760;
    areas.forEach((area) => {
      const coords = area.dataset.coords.split(',').map(Number);
      area.coords = coords.map((value, index) => Math.round(value * (area.shape === 'circle' && index === 2 ? Math.min(scaleX, scaleY) : index % 2 === 0 ? scaleX : scaleY))).join(',');
    });
  };
  if ('ResizeObserver' in window) new ResizeObserver(resizeAreas).observe(mapImage);
  window.addEventListener('resize', resizeAreas);
  mapImage.addEventListener('load', resizeAreas);
  resizeAreas();
}
