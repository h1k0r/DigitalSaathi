# Google AdSense Activation & Operational Guide

**Website:** [Vytra](https://vytra.in/)  
**Hosting Architecture:** 100% Static HTML/CSS/JavaScript on GitHub Pages  
**Target Ad Platform:** Google AdSense (Auto Ads & Non-Intrusive Responsive Units)  
**Configuration File:** [`config/ads-config.js`](file:///config/ads-config.js)  
**Authorization File:** [`ads.txt`](file:///ads.txt)  

---

## Overview

The Vytra codebase is pre-configured and architecturally hardened for Google AdSense site approval and monetization. All policy requirements have been satisfied:
- **Dedicated Legal Pages:** Up-to-date Privacy Policy, Cookie Policy, Terms of Service, About Us, and Contact Us.
- **In-Browser Processing Transparency:** Disclosures confirming files are never uploaded to servers.
- **Root `ads.txt` File:** Formatted per IAB standard and ready for your publisher ID.
- **Zero Layout Shift (CLS < 0.1):** Reserved ad slot heights and automatic collapse when ads are not active.
- **Client-Side Cookie Consent Banner:** Built-in GDPR/CCPA consent mode that controls ad script initialization.

---

## 10-Step AdSense Activation Checklist

### Step 1: Create or Sign In to Google AdSense
1. Visit the [Google AdSense Homepage](https://www.google.com/adsense/).
2. Sign in with your primary Google account.
3. If you do not have an active AdSense account, complete the account registration (selecting your country/territory and agreeing to the AdSense terms).

---

### Step 2: Add Vytra to Your AdSense Sites List
1. In the left navigation menu of the AdSense console, click **Sites**.
2. Click the **+ New site** (or **Add site**) button.
3. Enter your custom domain:
   ```
   vytra.in
   ```
4. Click **Save**.

---

### Step 3: Obtain Your Unique Publisher ID
Your Google AdSense Publisher ID is formatted as:
```
ca-pub-1234567890123456
```
*(Your numerical ID is 16 digits long).*

You can find this ID in:
- The AdSense code snippet displayed on screen.
- Or under **Account** > **Settings** > **Account information** in the AdSense console.

---

### Step 4: Update `ads.txt` with Your Authorized Publisher ID
Google crawlers verify domain ownership and ad fraud prevention using `/ads.txt`.

1. Open `ads.txt` in the root of your project:
   ```text
   google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0
   ```
2. Replace `pub-XXXXXXXXXXXXXXXX` with your actual numeric ID (without the `ca-` prefix):
   ```text
   google.com, pub-1234567890123456, DIRECT, f08c47fec0942fa0
   ```
3. Save the file.

---

### Step 5: Update Central Configuration (`config/ads-config.js`)
Vytra uses a single central script to manage all ad initialization and consent.

1. Open `config/ads-config.js`.
2. Locate the `ADSENSE_CONFIG` object:
   ```javascript
   const ADSENSE_CONFIG = {
     // 1. Change enabled to true:
     enabled: true,

     // 2. Insert your ca-pub ID:
     publisherId: "ca-pub-1234567890123456",

     // 3. Keep autoAds enabled (recommended by Google):
     autoAds: true,

     // 4. Leave devPlaceholder false for production:
     devPlaceholder: false,
     ...
   };
   ```
3. Save the file.

---

### Step 6: Commit and Deploy to GitHub Pages
Push your changes to the GitHub repository:
```bash
git add ads.txt config/ads-config.js
git commit -m "feat: activate Google AdSense publisher ID and authorized ads.txt"
git push origin main
```
Within 1–2 minutes, GitHub Pages will deploy the updated static build.

Verify your live `ads.txt` is accessible at:
```
https://vytra.in/ads.txt
```

---

### Step 7: Request Site Review in AdSense Console
1. Return to the **Sites** tab in the Google AdSense dashboard.
2. Under `vytra.in`, confirm the verification status method:
   - AdSense checks for the presence of the `pagead2.googlesyndication.com` script (which `config/ads-config.js` injects) and the `ads.txt` file.
3. Click **Request review**.
4. The review process typically takes between **24 hours and 14 days**.

---

### Step 8: Configure Auto Ads (Recommended Settings)
While your site is under review or once approved:
1. In AdSense, go to **Ads** > **By site**.
2. Click the edit icon (pencil) next to `vytra.in`.
3. Enable **Auto ads**.
4. Configure Ad formats for optimal user experience:
   - **In-page ads:** ON (Google places native responsive ads into natural breaks in content).
   - **Anchor ads:** ON (Docked banner at the top or bottom of mobile screens).
   - **Side rail ads:** ON (Displays on screens wider than 1000px in the margins).
   - **Vignette ads (Full screen):** Set frequency to **10 minutes or lower** so tool users are not interrupted while actively generating or converting files.
   - **Excluded areas:** If necessary, add an exclusion over the tool drag-and-drop interactive canvas (`.tool-workspace` or `#dropZone`).

---

### Step 9: Manual Ad Placement Rules (Accidental Click Protection)
If placing manual AdSense ad units (`<ins class="adsbygoogle">`):

| Placement Zone | Recommended Unit | Safety Distance | Policy Notes |
| :--- | :--- | :--- | :--- |
| **Top of Page (Below Breadcrumb)** | Responsive Leaderboard (`728x90` / `320x50`) | Minimum 24px above tool card | Never push tool controls below initial viewport. |
| **Below Tool Processing Area** | Responsive Large Rectangle (`336x280` / `300x250`) | Minimum 32px below Download button | Must never mimic download buttons or action triggers. |
| **Above Footer / Guide Section** | In-Article Horizontal Banner (`728x90`) | Natural flow | Labeled clearly with "Advertisement". |

> [!CAUTION]
> **AdSense Policy Strictness:**
> - Never place ad units immediately adjacent to file download buttons or dropzones.
> - Never label an ad with misleading text such as "Click here to download" or "Sponsored Link". Vytra includes standardized `.ad-label` ("ADVERTISEMENT").
> - Never click on your own live advertisements or encourage others to click them.

---

### Step 10: Post-Approval Health Monitoring
Once monetizing:
1. **Check `ads.txt` Status in AdSense:**
   - Confirm status shows **"Authorized"** (green checkmark).
2. **Monitor Core Web Vitals:**
   - In Google Search Console, verify **Cumulative Layout Shift (CLS)** remains `< 0.1`.
   - The `.adsense-slot` and `.ad-container` CSS classes enforce fixed minimum heights to guarantee zero layout shifts when ads render.
3. **Monitor Privacy / Consent:**
   - Vytra's built-in consent banner handles GDPR/CCPA storage preferences.
   - Users who click "Essential Only" will have ad containers collapsed automatically.
