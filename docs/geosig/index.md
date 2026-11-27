---
title: GeoSig – Cellular Signal Logger and Analytics
---

# GeoSig – Cellular Signal Logger and Analytics

![GeoSig – Cellular Signal Logger & Analytics](geosig-banner.jpg){ .bw-geo-banner }

<p class="bw-lead">A 5G/LTE RF field-survey app and live coverage map: record cellular signal quality with GPS on any Android phone, analyse it on the spot, and see every survey on a shared web map.</p>

<div class="bw-geo-actions" markdown>
[:material-map-marker-radius: Open the live coverage map](https://geosig.basigwireless.com){ .bw-btn .bw-btn--primary target="_blank" rel="noopener" }
[:material-android: Download the Android app (APK)](https://geosig.basigwireless.com/geosig.apk){ .bw-btn .bw-btn--outline }
</div>

<p class="bw-note">Requires Android 7.0 or later. The app asks for Precise Location and Phone State permissions to record signal measurements with GPS fixes. <a href="https://geosig.basigwireless.com/privacy" target="_blank" rel="noopener">Privacy policy</a></p>

## How It Works

<div class="bw-steps" markdown>

<div class="bw-step" markdown><span class="bw-step__n">1</span><span class="bw-step__icon">:material-cellphone-wireless:</span><strong>Record</strong><span>The app logs 5G/LTE measurements with GNSS position continuously, even in the background.</span></div>

<div class="bw-step" markdown><span class="bw-step__n">2</span><span class="bw-step__icon">:material-chart-bell-curve:</span><strong>Analyse</strong><span>Built-in labs compute shadow fading, path loss, distance to the cell and handover health on the phone.</span></div>

<div class="bw-step" markdown><span class="bw-step__n">3</span><span class="bw-step__icon">:material-cloud-sync:</span><strong>Sync & map</strong><span>Readings sync to the GeoSig server and appear on the live web map for anyone to explore.</span></div>

</div>

## App Features

<div class="bw-products bw-geo-features" markdown>

<div class="bw-product" markdown><span class="bw-product__media bw-product__media--icon">:material-access-point-network:</span><span class="bw-product__body" markdown><span class="bw-product__tag">Live</span><strong>Live Signal Dashboard</strong><span class="bw-product__desc">Serving-cell signal quality (RSRP, RSSI), cell identity (Cell ID/ECI, PCI, MCC-MNC, operator, network type), spectrum details (NR-ARFCN, DL/UL frequency, bandwidth), timing advance, GNSS fix and satellites, and dual-SIM support.</span></span></div>

<div class="bw-product" markdown><span class="bw-product__media bw-product__media--icon">:material-speedometer:</span><span class="bw-product__body" markdown><span class="bw-product__tag">Live</span><strong>Latency & Throughput Probe</strong><span class="bw-product__desc">Measures cellular latency (average, min/max ping), jitter and packet loss against a probe host, alongside the radio measurements.</span></span></div>

<div class="bw-product" markdown><span class="bw-product__media bw-product__media--icon">:material-swap-horizontal-bold:</span><span class="bw-product__body" markdown><span class="bw-product__tag">Analyzer</span><strong>Neighbor & Handover Analyzer</strong><span class="bw-product__desc">Serving-vs-neighbor RSRP timeline with handovers marked, handovers per minute, ping-pong detection, PCI collision and mod-3 interference checks, plus handover CSV export.</span></span></div>

<div class="bw-product" markdown><span class="bw-product__media bw-product__media--icon">:material-chart-histogram:</span><span class="bw-product__body" markdown><span class="bw-product__tag">ShadowLab</span><strong>Shadow-Fading Lab</strong><span class="bw-product__desc">Captures a 500-sample RSRP run and fits a Gaussian: mean, shadow σ, variance, P10/P50/P90, 90% fade margin and a log-normal interpretation of the clutter around you.</span></span></div>

<div class="bw-product" markdown><span class="bw-product__media bw-product__media--icon">:material-radio-tower:</span><span class="bw-product__body" markdown><span class="bw-product__tag">ITU PropLab</span><strong>ITU Propagation Lab</strong><span class="bw-product__desc">Applies the ITU-R M.2135 NLOS path-loss model to the measured RSRP to estimate distance to the cell (with a shadowing range), compares it with the LTE timing-advance distance, and plots path loss vs. distance. Carrier frequency is detected from the band; TX EIRP is adjustable.</span></span></div>

<div class="bw-product" markdown><span class="bw-product__media bw-product__media--icon">:material-map-search:</span><span class="bw-product__body" markdown><span class="bw-product__tag">Map</span><strong>On-Phone Coverage Map</strong><span class="bw-product__desc">Shows your survey trail, centres on your location, and uses logged GPS points to estimate cell-tower positions, with sectors and confidence for each tower.</span></span></div>

<div class="bw-product" markdown><span class="bw-product__media bw-product__media--icon">:material-file-delimited:</span><span class="bw-product__body" markdown><span class="bw-product__tag">Settings</span><strong>Logging, Export & Sync</strong><span class="bw-product__desc">Continuous background recording (resumes after reboot), drive-test readings and ShadowLab CSV exports, and sync to the central GeoSig server.</span></span></div>

<div class="bw-product" markdown><span class="bw-product__media bw-product__media--icon">:material-key-variant:</span><span class="bw-product__body" markdown><span class="bw-product__tag">Tracking</span><strong>10-Digit Tracking Key</strong><span class="bw-product__desc">Each phone gets a random 10-digit key. Enter it on the web map to follow that device's survey live, or generate a new key at any time.</span></span></div>

</div>

## Screenshots

=== "Live"

    <div class="bw-shots" markdown>
    <figure markdown>
    ![Serving-cell signal quality and cell identity](live-signal.jpg){ loading=lazy }
    <figcaption>Serving-cell signal quality and cell identity</figcaption>
    </figure>
    <figure markdown>
    ![Cellular latency and jitter probe](live-latency.jpg){ loading=lazy }
    <figcaption>Cellular latency and jitter probe</figcaption>
    </figure>
    </div>

=== "Neighbors & Handover"

    <div class="bw-shots" markdown>
    <figure markdown>
    ![Handover health and serving vs. neighbor cells](neighbors-handover.jpg){ loading=lazy }
    <figcaption>Handover health and serving vs. neighbor cells</figcaption>
    </figure>
    </div>

=== "ShadowLab"

    <div class="bw-shots" markdown>
    <figure markdown>
    ![500-sample shadow-fading capture](shadowlab-capture.jpg){ loading=lazy }
    <figcaption>500-sample shadow-fading capture</figcaption>
    </figure>
    <figure markdown>
    ![RSRP distribution with Gaussian fit](shadowlab-distribution.jpg){ loading=lazy }
    <figcaption>RSRP distribution with Gaussian fit</figcaption>
    </figure>
    <figure markdown>
    ![Shadow-fading parameters and insight](shadowlab-insight.jpg){ loading=lazy }
    <figcaption>Shadow-fading parameters and insight</figcaption>
    </figure>
    </div>

=== "ITU PropLab"

    <div class="bw-shots" markdown>
    <figure markdown>
    ![ITU-R M.2135 scenario and estimated distance](itu-scenarios.jpg){ loading=lazy }
    <figcaption>ITU-R M.2135 scenario and estimated distance</figcaption>
    </figure>
    <figure markdown>
    ![Path loss vs. distance curves](itu-pathloss.jpg){ loading=lazy }
    <figcaption>Path loss vs. distance curves</figcaption>
    </figure>
    <figure markdown>
    ![All ITU scenarios compared](itu-comparison.jpg){ loading=lazy }
    <figcaption>All ITU scenarios compared</figcaption>
    </figure>
    </div>

=== "Settings & Export"

    <div class="bw-shots" markdown>
    <figure markdown>
    ![CSV export and About GeoSig](settings-export.jpg){ loading=lazy }
    <figcaption>CSV export and About GeoSig</figcaption>
    </figure>
    </div>

## Live Coverage Map (Web)

Open [geosig.basigwireless.com](https://geosig.basigwireless.com){ target="_blank" rel="noopener" } in any browser to see all synced readings.

![GeoSig live coverage map showing survey routes across South India](web-map.jpg){ .bw-geo-web loading=lazy }

<div class="bw-related" markdown>

- **Signal-strength colours:** Excellent (≥ −80 dBm), Good (−81 to −100), Weak (−101 to −115) and Edge of coverage (≤ −116 dBm RSRP)
- **Filters:** date range (today, last 7 days or custom), operator, and optional low-accuracy GPS points
- **Live tracking:** follow one or more phones by their 10-digit keys; route and heatmap layers
- **Charts:** operator-wise RSRP distribution and radio-technology breakdown
- **Always current:** the map refreshes automatically every 10 seconds

</div>

<div class="bw-buybox" markdown>
<div markdown>
<p class="bw-kicker">GeoSig for your campus or network</p>
<h2 class="bw-h2">Coverage surveys, drive tests and training</h2>
<p>Email us about deploying GeoSig for your institution, or using it in a lab course or workshop.</p>
</div>
<a class="bw-btn bw-btn--primary" href="mailto:info@basigwireless.com">info@basigwireless.com</a>
</div>
